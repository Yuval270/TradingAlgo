from abc import ABC, abstractmethod
from quarter import Quarter
from pandas import Timestamp


class QuarterlyCycle(ABC):
    def __init__(self, duration_in_minutes: int, time_frame):
        self._duration_in_minutes = duration_in_minutes
        self._time_frame = time_frame

    @abstractmethod
    # todo we might change time_stamp type in the future to date or anything else
    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        pass
