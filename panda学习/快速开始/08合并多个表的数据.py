import pandas as pd
air_quality_no2 = pd.read_csv('../datas/air_quality_no2_long.csv')
air_quality_no2 = air_quality_no2[['date.utc','location','parameter','value']]
print(air_quality_no2.head())
air_quality_pm25 = pd.read_csv('../datas/air_quality_pm25_long.csv')
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]
print(air_quality_pm25.head())
print(air_quality_pm25.shape)
# 合并两张表
air_quality = pd.concat([air_quality_pm25,air_quality_no2],axis=0)
print(air_quality.shape)
# 合并两张表但是分层 不打乱顺序
# air_quality = pd.concat([air_quality_pm25,air_quality_no2],keys=["PM25", "NO2"])
# print(air_quality)
# print(air_quality.reset_index(level=0))

# 使用通用标识符联接表
stations_coord = pd.read_csv('../datas/air_quality_stations.csv')
print(stations_coord.head())

air_quality = pd.merge(air_quality,stations_coord,how='left',on='location')
print(air_quality)
# air_quality_parameter = pd.read_csv('../datas/air_quality_parameters.csv')
#
# print(air_quality_parameter.head())