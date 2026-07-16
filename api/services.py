import pandas as pd

def get_prices():

    df = pd.read_csv(
        "data/processed/brent_clean.csv"
    )

    return df.to_dict(
        orient="records"
    )
def get_change_points():

    df = pd.read_csv(
        "data/processed/change_points.csv"
    )

    return df.to_dict(
        orient="records"
    )

def get_events():

    df = pd.read_csv(
        "data/processed/events_clean.csv"
    )

    return df.to_dict(
        orient="records"
    )
def get_event_matches():

    df = pd.read_csv(
        "data/processed/event_matches.csv"
    )

    return df.to_dict(
        orient="records"
    )