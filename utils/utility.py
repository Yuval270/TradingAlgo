from datetime import datetime
import pytz


def get_fixed_time():
    return datetime.now(pytz.timezone('America/New_York'))


def get_current_year_seconds_amount():
    current_year = datetime.now().year

    start_of_year = datetime(current_year, 1, 1)
    end_of_year = datetime(current_year + 1, 1, 1)

    return (end_of_year - start_of_year).total_seconds()
