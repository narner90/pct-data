import pickle

import pandas as pd


class ActivitySummaryWriter:
    def __init__(self):
        pass

    def write_summary(self, summary: pd.DataFrame) -> None:
        with open('./data/activity_summary.pkl', 'wb') as file:
            pickle.dump(summary, file)
