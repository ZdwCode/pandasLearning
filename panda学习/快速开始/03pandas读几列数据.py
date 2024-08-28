import pandas as pd

titanic = pd.read_csv('titanic.csv')
print(titanic.info())
print(titanic['Age'].head())  # type Series
print(titanic['Age'].shape)  # (891,)

# 取特定的列
index = ['Age', 'Name']
print(titanic[index].head())  # 在[]里面放一个列表
print(titanic[index].shape)  # (891,2)
# 取特定的行
print(titanic[titanic['Age'] > 35].shape)  # (217, 12)
print(titanic[titanic['Pclass'].isin([2, 3])].head(20))  # 等价于 titanic[titanic['Pclass']==2 | titanic['Pclass']==3]
# 特定的行 特定的列
print(titanic.loc[titanic['Age'] > 35, ['Name','Fare']])
print(titanic.iloc[9:25, 2:5])