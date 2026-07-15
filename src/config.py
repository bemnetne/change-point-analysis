from pathlib import Path

# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
HISTORICAL_DATA_DIR = ROOT_DIR / "data" / "historical_data"

BRENT_DATA = RAW_DATA_DIR / "BrentOilPrices.csv"
EVENT_DATA = HISTORICAL_DATA_DIR / "events.csv"
PROCESSED_EVENT_DATA = PROCESSED_DATA_DIR / "events_clean.csv"
# Figures
FIGURE_DIR = ROOT_DIR / "reports" / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)