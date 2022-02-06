import pandas as pd


class ServerEnvironment:
    def __init__(self):
        self._summary = pd.read_pickle('../data/activity_summary.pkl')

    def get_summary(self) -> str:
        return self._summary.to_dict()
