import pandas as pd
import matplotlib.pyplot as plt
air_quality = pd.read_csv('../datas/air_quality_no2_long.csv')
air_quality = air_quality.rename(columns=({'date.utc': "datetime"}))
air_quality['datetime'] = pd.to_datetime(air_quality['datetime'])
print(air_quality.head())
print(air_quality['datetime'].max())