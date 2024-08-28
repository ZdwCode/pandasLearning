import numpy as np
import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

d = pd.DataFrame(d,index=['b','c'],columns=['two','three']) # 数据 指定行 指定列
print(d)

# 增加和删除
d['one'] = pd.Series([1.0, 2.0, 3.0]) # 一般在最后一行插入
d.insert(0,'bar',d["two"]) # 位置 列名 值
print(d)
# del d['bar']
# print(d)

d = d.assign(ratio=d['bar']/d['two']) # 通过方法链中增加新的列 assgin总是返回数据的副本，保留原始数据 数据帧未受影响
print(d)
