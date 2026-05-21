from pathlib import Path

import pandas as pd


TRANSFORMED_PATH = Path("data/transformed/events.csv")
FEATURES_PATH = Path("data/features/events.csv")


def main() -> None:
    events = pd.read_csv(TRANSFORMED_PATH)
    events["duration_minutes"] = events["duration_seconds"] / 60
    events["weekday"] = pd.to_datetime(events["date"]).dt.day_name()

    FEATURES_PATH.parent.mkdir(parents=True, exist_ok=True)
    events.to_csv(FEATURES_PATH, index=False)


if __name__ == "__main__":
    main()
