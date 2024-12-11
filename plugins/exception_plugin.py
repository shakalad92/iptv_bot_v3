class ExceptionPlugin:
    def __init__(self):
        self.failures = []

    def pytest_runtest_logreport(self, report):
        if report.failed and report.when == 'call':
            self.failures.append(report)
