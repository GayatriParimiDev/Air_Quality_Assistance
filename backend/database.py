# backend/database.py
import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz
DATA_FILE = "data/globalAirQuality.csv"   # <- uses your uploaded file

# Load dataset
def _load():
    try:
        df = pd.read_csv(DATA_FILE)
    except Exception as e:
        raise RuntimeError(f"Failed to load dataset at {DATA_FILE}: {e}")

    # normalize column names
    df.columns = [c.strip() for c in df.columns]

    # try to find AQI column (case-insensitive common names)
    aqi_candidates = [c for c in df.columns if c.lower() in ("aqi","air_quality_index","aqivalue","aqi_value","aqi value")]
    if aqi_candidates:
        aqi_col = aqi_candidates[0]
    else:
        # fallback: find numeric column with name containing 'aq' or 'index'
        aqi_col = None
        for c in df.columns:
            if ('aq' in c.lower() or 'index' in c.lower()) and pd.api.types.is_numeric_dtype(df[c]):
                aqi_col = c
                break

    if aqi_col is None:
        # choose first numeric column as AQI fallback
        numerics = df.select_dtypes(include=np.number).columns.tolist()
        if not numerics:
            raise RuntimeError("No numeric columns found to use as AQI.")
        aqi_col = numerics[0]

    # ensure columns exist for city/country
    city_col = next((c for c in df.columns if c.lower() in ("city","town","location")), None)
    country_col = next((c for c in df.columns if c.lower() in ("country","nation")), None)

    if city_col is None:
        df["city"] = "Unknown"
        city_col = "city"
    else:
        df.rename(columns={city_col: "city"}, inplace=True)
        city_col = "city"

    if country_col is None:
        df["country"] = "Unknown"
        country_col = "country"
    else:
        df.rename(columns={country_col: "country"}, inplace=True)
        country_col = "country"

    # rename aqi column to AQI
    if aqi_col != "AQI":
        df.rename(columns={aqi_col: "AQI"}, inplace=True)

    # Ensure numeric AQI
    df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")

    # Standardize city names
    df["city"] = df["city"].astype(str).str.strip()
    df["city_lower"] = df["city"].str.lower()

    # Groupby city: compute mean for numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    agg = df.groupby("city").agg({**{c: "mean" for c in numeric_cols}, "country": lambda x: x.mode().iat[0] if not x.mode().empty else "Unknown"}).reset_index()
    # Round numbers for neatness
    for c in numeric_cols:
        agg[c] = agg[c].round(2)

    # create city name list for fuzzy matching
    city_list = agg["city"].tolist()

    return df, agg, city_list

RAW_DF, CITY_AGG, CITY_NAMES = _load()


def find_best_city(query, score_cutoff=60):
    """Return best matching city name and score, or (None,0)"""
    if not query:
        return None, 0
    # use rapidfuzz process.extractOne
    best = process.extractOne(query, CITY_NAMES, scorer=fuzz.WRatio)
    if best is None:
        return None, 0
    name, score, idx = best
    if score >= score_cutoff:
        return name, score
    return None, score


def get_city_aqi(city_name):
    """Return aggregated row dict for a city name (exact match) or None"""
    row = CITY_AGG[CITY_AGG["city"].str.lower() == city_name.strip().lower()]
    if row.empty:
        return None
    return row.iloc[0].to_dict()


def top_n_polluted(n=10):
    return CITY_AGG.sort_values("AQI", ascending=False).head(n).to_dict(orient="records")
