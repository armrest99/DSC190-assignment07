from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/events.csv")
CLEAN_PATH = Path("data/clean/events.csv")
VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}


def main() -> None:
    events = pd.read_csv(RAW_PATH)
    events = events.dropna()

    events["duration_seconds"] = pd.to_numeric(
        events["duration_seconds"], errors="coerce"
    )
    events["timestamp"] = pd.to_datetime(
        events["timestamp"], format="mixed", errors="coerce"
    )

    events = events[
        events["user_id"].astype(str).str.strip().ne("")
        & events["event_type"].isin(VALID_EVENT_TYPES)
        & events["duration_seconds"].gt(0)
        & events["timestamp"].notna()
    ].copy()

    events["timestamp"] = events["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")
    events["duration_seconds"] = events["duration_seconds"].astype(int)

    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    events.to_csv(CLEAN_PATH, index=False)


if __name__ == "__main__":
    main()
