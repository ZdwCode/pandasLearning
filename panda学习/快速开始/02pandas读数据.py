import pandas as pd
titanic = pd.read_csv('titanic.csv')
print(titanic.head(8))
print(titanic.tail(8))
print(titanic.dtypes)
print(titanic.info())
# titanic.to_excel('titanic.xlsx',index=False,sheet_name='passengers')