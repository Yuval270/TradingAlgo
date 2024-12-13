import tvDatafeed
from tvDatafeed import TvDatafeed, Interval

tv = TvDatafeed()


data = tv.get_hist(
        "NAS100",
        "PEPPERSTONE",
        interval=Interval.in_1_hour,
        n_bars=1,
    )
print(data.to_dict())
print(data.iloc[0]['open'])
print(data.iloc[0]['symbol'])
print(f"tiemstamp is {data.index[0]}")