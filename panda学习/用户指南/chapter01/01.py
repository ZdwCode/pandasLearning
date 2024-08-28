import numpy as np
import pandas as pd

# 创建一列
date = pd.date_range('20220102',periods=6)
s = pd.Series([1, 3, 5, np.nan, 6, 8],index=date)
print(s.head())
# 创建一个dataframe
s2 = pd.DataFrame(np.random.randn(6,4),index=date,columns=list('ABCD'))
print(s2)
# 使用字典创建一个dataframe
s3 = pd.DataFrame({
    "A": 1.0,
    "B": np.random.random(4),
    "C": pd.date_range('20220102',periods=4),
    "D": pd.Categorical(["test", "train", "test", "train"]),
})
print(s3)
print(s3.to_numpy())
print(s2.sort_index())
print(s2.sort_index(axis=1,ascending=False))
print(s2.sort_values(by="A"))

# dateframe的选择
# 选择一列
print(s2['A'])
# 0-3 行
print(s2[0:3])
print(s2[0:3][['A','B']])
# print(s2[0:3]['A':'B']) 出错 只有行才可以按切片来
# 通过loc方法来按标签选择
print(s2.loc[date[0]]) # 某一行的数据
# 某行 某列
print(s2.loc[:,["A","C"]])

# 使用iloc 某行某列 可以使用切片 也可以选择特定的行和列
print(s2.iloc[:,:])

# 使用判断语句来选择
print(s2[s2['A']>0])