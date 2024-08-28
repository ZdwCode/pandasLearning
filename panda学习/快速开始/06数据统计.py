import pandas as pd
titanic = pd.read_csv('titanic.csv')
print(f'titanic\'s mean(Age):{titanic["Age"].mean()}')
print(f'titanic\'s median(Age,Fare):{titanic[["Age","Fare"]].mean()}')
print(f'titanic\'s describe:{titanic["Age"].describe()}')

# 自定义属性
result = titanic.agg(
    {
        "Age":["min", "max", "median", "skew"],
        "Fare":["min", "max", "median", "skew"]
    }
)
print(titanic[["Sex", "Age"]].groupby('Sex').max())
print(titanic.groupby('Sex').mean(numeric_only=True))
print(titanic.groupby(['Sex','Pclass'])['Fare'].mean())