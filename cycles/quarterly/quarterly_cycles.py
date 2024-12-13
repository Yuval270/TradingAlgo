from utils import time_constants as time_constants
from cycles.quarterly.quarterly_cycle import QuarterlyCycle


class YearlyCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_CURRENT_YEAR, "PlaceHolder")


class TwentyFiveDaysCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_22_5_DAYS, "PlaceHolder")


class MonthlyCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_1_WEEK, "PlaceHolder")


class WeeklyCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_1_DAY, "PlaceHolder")


class DailyCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_6_HOURS, "PlaceHolder")


class SessionCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_90_MINUTES, "PlaceHolder")


class MicroCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_22_5_MINUTES, "PlaceHolder")


class NanoCycle(QuarterlyCycle):
    def __init__(self):
        super().__init__(time_constants.SECONDS_IN_5_5_MINUTES, "PlaceHolder")
