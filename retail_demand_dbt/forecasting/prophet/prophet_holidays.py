import pandas as pd


def prepare_holidays(calendar_file):
    calendar = pd.read_csv(calendar_file)

    holidays = []

    for column in ["event_name_1", "event_name_2"]:
        events = calendar[calendar[column].notna()][["date", column]].copy()
        events = events.rename(columns={column: "holiday"})
        holidays.append(events)

    return pd.concat(holidays, ignore_index=True)[["holiday", "date"]].rename(
        columns={"date": "ds"}
    )