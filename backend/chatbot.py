# backend/chatbot.py
from database import find_best_city, get_city_aqi, top_n_polluted
from utils import categorize_aqi, health_precautions

import re

def parse_city_from_text(text):
    # look for patterns like "in <city>" or "for <city>"
    m = re.search(r"(?:in|at|for)\s+([A-Za-z\s\-\']{2,60})", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: if single word query maybe it's the city itself
    words = text.split()
    if len(words) <= 3:
        return text.strip()
    return None

def generate_aqi_reply_for_city(city_query):
    if not city_query:
        return "I couldn't identify the city. Ask like: 'What is the AQI in Delhi?'"

    best_name, score = find_best_city(city_query)
    if not best_name:
        # try returning suggestions (top fuzzy matches)
        return f"Couldn't find a close match for '{city_query}'. Try a different city name or check spelling."

    data = get_city_aqi(best_name)
    if not data:
        return f"Data for '{best_name}' not found."

    aqi = data.get("AQI", "Unknown")
    category = categorize_aqi(aqi)
    precautions = health_precautions(aqi)
    country = data.get("country", "Unknown")

    # build message
    msg = f"🌍 Air Quality — {best_name} ({country})\n"
    msg += f"AQI: {aqi}  •  Category: {category}\n\n"
    # include some pollutant info if available
    pollutant_keys = [k for k in data.keys() if k.lower() in ("pm2.5","pm2_5","pm25","pm10","no2","so2","o3","co")]
    for k in pollutant_keys[:6]:
        v = data.get(k)
        msg += f"{k}: {v}  \n"
    msg += f"\n⚕️ Precautions: {precautions}"
    return msg

def handle_message(text):
    text = (text or "").strip()
    if not text:
        return "Please ask something about AQI like: 'What is the AQI in Mumbai?'"

    text_lower = text.lower()

    # top polluted intent
    if "top" in text_lower and ("pollut" in text_lower or "worst" in text_lower or "highest" in text_lower):
        n_match = re.search(r"top\s+(\d+)", text_lower)
        n = int(n_match.group(1)) if n_match else 10
        recs = top_n_polluted(n)
        lines = [f"{i+1}. {r['city']} ({r.get('country','')}) — AQI: {r.get('AQI')}" for i,r in enumerate(recs)]
        return "Top polluted cities:\n\n" + "\n".join(lines)

    # direct AQI question
    if "aqi" in text_lower or "air quality" in text_lower:
        city = parse_city_from_text(text)
        if city:
            return generate_aqi_reply_for_city(city)
        # maybe the message is just the city name
        if len(text.split()) <= 3:
            return generate_aqi_reply_for_city(text)
        return "I detected an AQI question but couldn't parse the city. Ask like: 'What's the AQI in London?'"

    # if user asks for help
    if any(w in text_lower for w in ("help","how to","what can you do")):
        return ("I can answer AQI questions. Examples:\n"
                "- What is the AQI in New York?\n"
                "- Show top 5 polluted cities\n"
                "- What precautions to take if AQI is high?\n")

    # default fallback: treat as city name maybe
    if len(text.split()) <= 3:
        return generate_aqi_reply_for_city(text)

    return "Sorry, I didn't understand. Ask about AQI (e.g., 'AQI in Tokyo') or 'help' for examples."
