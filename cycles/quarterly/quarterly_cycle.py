from abc import ABC

import pandas as pd

from utils.time_constants import START_OF_THE_DAY_IN_HOUR
from cycles.quarterly.quarter import Quarter
from pandas import Timestamp

import utils.utility as utils


class QuarterlyCycle(ABC):
    def __init__(self, duration_in_seconds: int, time_frame):
        self._duration_in_seconds = duration_in_seconds
        self._time_frame = time_frame

    def get_current_quarter(self, time_stamp: Timestamp = None) -> Quarter:
        if time_stamp is None:
            time_stamp = utils.get_fixed_time()

        start_of_day = time_stamp.replace(hour=START_OF_THE_DAY_IN_HOUR, minute=0, second=0, microsecond=0)

        # Convert the timestamp to a time in seconds since the start of the trading day 18:00
        if time_stamp < start_of_day:
            start_of_day -= pd.DateOffset(days=1)

        seconds_since_start = (time_stamp - start_of_day).total_seconds()
        quarter_index = (seconds_since_start // self._duration_in_seconds) % 4

        return Quarter(quarter_index)
