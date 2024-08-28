import numpy as np
import pandas as pd

index = ['a','b','c','d','d']
data = np.random.randn(5)
s = pd.Series(data, index=index, name='something')
print(s)
print(s.index)
print(s.values)
s1 = pd.Series(np.random.randn(5))
print(s1)
print(s1.index)
print(s.dtypes)
print(s.get('f',np.nan))
print(s.name)