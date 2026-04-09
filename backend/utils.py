# backend/utils.py

def categorize_aqi(aqi):
    try:
        aqi = float(aqi)
    except:
        return "Unknown"
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Moderate"
    if aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    if aqi <= 200:
        return "Unhealthy"
    if aqi <= 300:
        return "Very Unhealthy"
    return "Hazardous"

def health_precautions(aqi):
    try:
        aqi = float(aqi)
    except:
        return "No data to provide precautions."

    if aqi <= 50:
        return "Air quality is good. No special precautions."
    if aqi <= 100:
        return "Moderate: sensitive people should reduce intense outdoor exercise."
    if aqi <= 150:
        return "Unhealthy for Sensitive Groups: wear a mask outdoors and limit prolonged exertion."
    if aqi <= 200:
        return "Unhealthy: wear N95/FFP2 mask outside; avoid outdoor activities."
    if aqi <= 300:
        return "Very Unhealthy: stay indoors with windows closed; use air purifiers if available."
    return "Hazardous: avoid outdoor exposure; seek medical help if symptoms appear."
