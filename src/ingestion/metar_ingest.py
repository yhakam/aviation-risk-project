import os 
import requests
import pandas as pd
from datetime import datetime, timezone

def fetch_metar(icao : str = "LFPG", hours : int = 1)-> pd.DataFrame:
    url = "https://aviationweather.gov/api/data/metar"
    params = {"ids": icao, "hours": hours, "format" : "json"}
    response = requests.get(url, params=params, timeout = 30)
    response.raise_for_status()
    data = response.json()
    if isinstance(data,dict):
        metars = data.get("data",[])
    elif isinstance(data,list):
        metars = data
    else:
        metars = []
        
    if not metars:
        print(f"Aucun metars récupéré pour {icao}")
        return pd.DataFrame()
    
    df = pd.json_normalize(metars)

    df["fetch_time_utc"]=datetime.now(timezone.utc)

    return df

def save_metar_to_csv(df: pd.DataFrame, icao : str="LFPG")->str:
    os.makedirs("data/raw", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/metar_{icao}_{timestamp}.csv"
    df.to_csv(filename, index = False)
    return filename

if __name__ == "__main__":
    icao = "LFPG"
    print(f"Recupération des METAR pour {icao}...")
    df = fetch_metar(icao=icao, hours = 1)

    if df.empty:
        print("Aucun METAR récupéré")
    else:
        print(f"Nombre de METAR récupéré:{len(df)}")
        print(df.head())

        filepath = save_metar_to_csv(df, icao=icao)
        print(f"Données METAR sauvegardées dans : {filepath}")