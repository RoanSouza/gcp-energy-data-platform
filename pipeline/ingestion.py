# ingestion.py - simulação de ingestão para camada raw
import pandas as pd

def generate_sample():
    data = {
        "date": pd.date_range("2021-01-01", periods=12, freq="M"),
        "consumo_mwh": [1000,1200,1100,1500,1700,1800,2000,1900,2100,2200,2300,2400],
        "city": ["Rio","SP","BH","Curitiba","Fortaleza","Recife","Manaus","POA","Salvador","Brasilia","Niteroi","Campinas"]
    }
    df = pd.DataFrame(data)
    df.to_csv("energy_data_raw.csv", index=False)
    print("Arquivo salvo: energy_data_raw.csv")

if __name__ == '__main__':
    generate_sample()
