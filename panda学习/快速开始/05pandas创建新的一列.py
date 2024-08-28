import pandas as pd
air_qualtiy = pd.read_csv('../datas/air_quality.csv', index_col=0, parse_dates=True)
print(air_qualtiy.head())
air_qualtiy['london_mg_per_cubic'] = air_qualtiy['station_london'] * 1.882  # 所有的列都乘
print(air_qualtiy.head())
air_qualtiy["ratio_paris_antwerp"] = (
    air_qualtiy["station_paris"] / air_qualtiy["station_antwerp"]
)
print(air_qualtiy.head())