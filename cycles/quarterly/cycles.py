from pandas import Timestamp

from quarter import Quarter
from cycle import QuarterlyCycle


class YearlyCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class TwentyFiveDaysCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class MonthlyCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class WeeklyCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class DailyCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class SessionCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class MicroCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass


class NanoCycle(QuarterlyCycle):
    def __init__(self, duration_in_minutes: int):
        super().__init__(duration_in_minutes, "PlaceHolder")

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass
