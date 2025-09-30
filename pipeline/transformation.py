# transformation.py - transformação simples
import pandas as pd

def transform():
    df = pd.read_csv("energy_data_raw.csv")
    df["consumo_kwh"] = df["consumo_mwh"] * 1000
    df.to_csv("energy_data_refined.csv", index=False)
    print("Transformação concluída: energy_data_refined.csv")

if __name__ == '__main__':
    transform()
