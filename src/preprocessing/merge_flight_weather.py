import os
import glob
import pandas as pd
from datetime import datetime, timezone
import sys

def get_latest_file(pattern : str):
    files = glob.glob(pattern)

    if not files:
        return None
    files.sort(reverse=True)
    return files[0]

def merge_flights_with_weather(flights_df : pd.DataFrame, metar_df : pd.DataFrame)->pd.DataFrame:

    if metar_df.empty :
        print("Metar vide")
        return flights_df
    
    if "fetch_time_utc" in metar_df.columns:
        metar_df=metar_df.sort_values(by="fetch_time_utc", ascending = False)

    latest_metar = metar_df.iloc[0].to_dict()
    metar_cols = {f"metar_{k}": v for k, v in latest_metar.items()}

    enriched = flights_df.assign(**metar_cols)

    return enriched
def save_enriched(df : pd.DataFrame)-> str:
    os.makedirs("data/processed", exist_ok = True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"data/processed/flights_enriched_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename

if __name__ == "__main__":
    flights_file = get_latest_file("data/raw/opensky_states_*.csv")
    metar_file = get_latest_file("data/raw/metar_*.csv")

    if flights_file is None:
        print("Aucun fichier OpenSky n'a été trouvé dans data/raw")
        sys.exit(1)

    if metar_file is None:
        print("Aucun fichier METAR n'a été trouvé dans data/raw")
        sys.exit(1)

    print(f"Fichier vols  : {flights_file}")
    print(f"Fichier METAR : {metar_file}")

    flights_df = pd.read_csv(flights_file)
    metar_df = pd.read_csv(metar_file)

    print(f"Vols chargés   : {len(flights_df)} lignes")
    print(f"METAR chargés  : {len(metar_df)} lignes")

    enriched_df = merge_flights_with_weather(flights_df, metar_df)
    print(f"Lignes après enrichissement : {len(enriched_df)}")

    out_path = save_enriched(enriched_df)
    print(f"Le fichier enrichi est enregistré dans : {out_path}")