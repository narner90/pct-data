import pickle
from datetime import datetime

import pandas as pd
from stravalib.client import Client


class ActivitySummaryLoader:
    def __init__(self):
        self._client = Client()

    def load_summary(self) -> pd.DataFrame:
        with open('./secret/access_token.pkl', 'rb') as file:
            token = pickle.load(file)

        self._client.access_token = token
        athlete = self._client.get_athlete()
        print(f'Loaded athlete: {athlete.firstname} {athlete.lastname}')

        print(f'Loading activities')
        activities = self._client.get_activities(limit=1000)
        print(f'Filtering activities')
        filtered_activities = self._filter_activities(activities)
        print(f'Creating summary')
        return self._summarize(filtered_activities)

    def _filter_activities(self, activities) -> list:
        return list(filter(lambda x: x.name.startswith('Day '), activities))

    def _summarize(self, activities) -> pd.DataFrame:
        summary_dict = {
            'elev_high': [a.elev_high for a in activities],
            'elev_low': [a.elev_low for a in activities],
            'km': [float(a.distance / 1000) for a in activities],
            'label': [a.name for a in activities],
            'total_elevation_gain': [float(a.total_elevation_gain) for a in activities],
            'activity_id': [a.id for a in activities],
            'date': [datetime.date(a.start_date) for a in activities]
        }
        return pd.DataFrame.from_dict(summary_dict).dropna()
