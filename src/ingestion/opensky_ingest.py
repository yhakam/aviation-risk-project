import os
import requests
import pandas as pd
from datetime import datetime, timezone

OPENSKY_USER = os.getenv("OPENSKY_USER")
OPENSKY_PASS = os.getenv("OPENSKY_PASS")

def fetch_opensky_states():
    url = "https://opensky-network.org/api/states/all"
    auth = (OPENSKY_USER, OPENSKY_PASS) if OPENSKY_USER and OPENSKY_PASS else None
    response = requests.get(url, auth=auth, timeout=30)
    response.raise_for_status()
    data = response.json()
    states = data.get("states",[])
    cols = ["icao24", "callsign", "origin_country", "time_position", "last_contact",
        "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
        "true_track", "vertical_rate", "sensors", "geo_altitude", "squawk",
        "spi", "position_source"]
    df = pd.DataFrame(states, columns=cols)
    df["fetch_time_utc"] = datetime.now(timezone.utc)
    return df

def save_states_to_csv(df: pd.DataFrame)-> str:
    
    os.makedirs("data/raw", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/opensky_states_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename

if __name__ == "__main__":
    print("Récuperation des vols en cours via OpenSky...")
    df = fetch_opensky_states()
    print(f"Nombre de lignes recupérés : {len(df)}")
    print(df.head())

    filepath=save_states_to_csv(df)
    print(f"Données sauvegardées dans : {filepath}")