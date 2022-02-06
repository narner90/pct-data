from pct_data.loader.activity_summary_loader import ActivitySummaryLoader
from pct_data.loader.activity_summary_writer import ActivitySummaryWriter


class Runner:
    def __init__(self):
        pass

    def run(self):
        activities_loader = ActivitySummaryLoader()
        summary = activities_loader.load_summary()
        summary_writer = ActivitySummaryWriter()
        summary_writer.write_summary(summary)


if __name__ == '__main__':
    Runner().run()
