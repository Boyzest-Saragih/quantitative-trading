import os
import pandas as pd


def load_data (path : str) -> pd.DataFrame:
    column_names = ['Date','Time','Open','High','Low','Close','Volume']

    df = pd.read_csv(path, skiprows=1, names=column_names)

    df['DateTime'] = pd.to_datetime(df["Date"].astype(str)+' '+ df['Time'])

    df = df.drop(columns=['Date', 'Time'])

    df = df[['DateTime','Open','High','Low','Close','Volume']]

    df.set_index('DateTime', inplace=True)

    print(f'Dataset OK!, jumlah: {len(df)}')
    return df

def validate_timestamp (df: pd.DataFrame):

    # Cek apakah index terurut dari waktu terlama ke terbaru
    is_monotonic = df.index.is_monotonic_increasing
    print(f"Motonic Increasing? {is_monotonic}")

    if not is_monotonic:
        print("Data tidak berurutan secara kronologis! Menyortir indeks...")
        df.sort_index(inplace=True)
    
    # Cek selisih waktu (time delta) antar baris berturutan
    time_deltas = df.index.to_series().diff()

    # Untuk M15, selisih normal = 15 menit (exc: weekend / market close)
    abnormal_intervals = time_deltas[time_deltas > pd.Timedelta(minutes=15)]
    print(f"Jumlah celah waktu (gaps akibat market close/weekend): {len(abnormal_intervals)}")

def check_missing (df: pd.DataFrame) -> pd.Series:
    missing_values = df.isnull().sum()
    print("\n Pengecekan Missing Values (NaN):")
    for col, count in missing_values.items():
        print(f"   - Kolom {col}: {count} data kosong")
    
    return missing_values

def check_duplicate (df: pd.DataFrame) -> int:
    duplicate_count = df.index.duplicated().sum()
    print(f"\n Pengecekan Data Duplikat:")
    print(f"   - Ditemukan {duplicate_count} data dengan timestamp kembar.")
    
    if duplicate_count > 0:
        print("   - Mengatasi duplikat dengan mempertahankan baris pertama...")
        # Menghapus duplikat pada indeks jika ditemukan
        df = df[~df.index.duplicated(keep='first')]
        
    return duplicate_count


file_path = "data/raw/2026.7.13XAUUSD-M15-No Session.csv"
data = load_data(file_path)
validate_timestamp(data)
check_missing(data)
check_duplicate(data)