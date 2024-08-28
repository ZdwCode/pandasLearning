import pandas as pd
#titanic = pd.read_csv('../datas/titanic.csv')
air_quality = pd.read_csv('../datas/air_quality_long.csv',index_col='date.utc')
print(air_quality.head())
# print(titanic.head())
# print(titanic.sort_values(by="Age",ascending=False)["Age"].head())
# print(titanic.sort_values(by=["Age","Pclass"],ascending=False))
no2 = air_quality[air_quality["parameter"] == 'no2']
no2_subset = no2.sort_index().groupby(["location"]).head(5)
print(no2_subset['location'])