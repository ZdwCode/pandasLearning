import pandas as pd

mydataframe = pd.DataFrame(
    {
        "name":['Zhang Dengwei','Zhang Chengyu','Tao Andong'],
        "age":[10,20,30],
        "sex":[0,1,0]
    }
)
print(mydataframe.describe())

age = pd.Series([10,20,30],name='age')
print(age)