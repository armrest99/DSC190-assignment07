import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd

    return mo, pd, plt


@app.cell
def _(pd):
    events = pd.read_csv("data/features/events.csv")
    return (events,)


@app.cell
def _(events, plt):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(events["duration_minutes"], bins=20, edgecolor="white")
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of events")
    fig.tight_layout()
    return (fig,)


if __name__ == "__main__":
    app.run()
