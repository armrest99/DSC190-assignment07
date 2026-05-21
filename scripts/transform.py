from pathlib import Path

import pandas as pd


CLEAN_PATH = Path("data/clean/events.csv")
TRANSFORMED_PATH = Path("data/transformed/events.csv")


def main() -> None:
    events = pd.read_csv(CLEAN_PATH)
    events["date"] = pd.to_datetime(events["timestamp"]).dt.strftime("%Y-%m-%d")

    TRANSFORMED_PATH.parent.mkdir(parents=True, exist_ok=True)
    events.to_csv(TRANSFORMED_PATH, index=False)


if __name__ == "__main__":
    main()
