from pct_data.data.activity_summary_loader import ActivitySummaryLoader


class Runner:
    def __init__(self):
        pass

    def run(self):
        activities_loader = ActivitySummaryLoader()
        print(activities_loader.load_activities())


if __name__ == '__main__':
    Runner().run()
