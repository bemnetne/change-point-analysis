import pandas as pd
import numpy as np


def load_oil_data(filepath):
    """
    Load Brent oil price dataset.
    """
    return pd.read_csv(filepath)

def load_event_data(filepath):
    """
    Load Brent oil price dataset.
    """
    return pd.read_csv(filepath)

def preprocess_dates(df):
    """
    Convert Date column to datetime and sort data.
    """
    df["Date"] = pd.to_datetime(df["Date"], format="mixed")

    df = df.sort_values("Date").reset_index(drop=True)

    return df


def compute_log_returns(df):
    """
    Compute log prices and log returns.
    """

    df["LogPrice"] = np.log(df["Price"])

    df["LogReturn"] = df["LogPrice"].diff()

    return df.dropna().reset_index(drop=True)


def compute_rolling_volatility(df, window=30):

    df["RollingVolatility"] = (
        df["LogReturn"]
        .rolling(window)
        .std()
    )

    return df