import random

import pandas as pd
import numpy as np
s = pd.Series([1,3,4,np.nan,6,8])
print(s)
dates = pd.date_range('20230222',periods=6)
print(dates.values)
df = pd.DataFrame(np.random.randn(6, 4),index=dates,columns=list("ABCD"))
print(df)

df2 = pd.DataFrame({
    'A': 1.0,
    'B': pd.Timestamp("20230226"),
    'C': pd.Series(1, index=list(range(3)), dtype="float32"),
    'D': np.array([3]*3,dtype="int32"),
    'E': pd.Categorical(['test','train','train']),
    'F': "foo",
})
#
# print(df2)
#
# df3 = pd.DataFrame(np.random.randn(6, 4))
# print(df3.to_numpy())

# 按内容选择
print(df['A'])
#print(df[0:3])
print(df["20230222":"20230205"])
print(df.loc[dates[0]]['A'])
print(df.loc[:, ["A","B"]])
print(df.loc["2023-02-22":"2023-02-25", ["A","B"]])

# 按索引选择选择
print('按职位选择')
print(df.iloc[3, 2])  # 前面是行 后面是列

# 布尔索引
print(df[df['A'] > 0])
# 使用isin进行过滤
df3 = df.copy()
df3['E'] = ["one", "one", "two", "three", "four", "three"]
print(df3[df3['E'].isin(['two', 'four'])])
# 设置
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range("20230222",periods=6))
print(s1)
df['F'] = s1
print(df)
print('按标签设置值')
df.at[dates[0],'A'] = 0
print(df)

# 缺失数据
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0:2],"E"] = 1
print(df1)
print('剔除缺省值')
df1.dropna(how="any")
print(df1.dropna(how="any"))
# 填充缺省值
print(df1.fillna(value=2))
print(df1)

# 自定义函数应用
print(df.apply(np.cumsum))
print(df.apply(lambda x:x.max()-x.min()))

# 统计
s = pd.Series(np.random.randint(0, 7, size=10))
print(s.value_counts())
# 分组
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df.groupby("A").max())