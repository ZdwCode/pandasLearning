import pandas as pd

df = pd.read_excel('work.xlsx', header=None)
index = 0
new_col_0 = []
new_col_1 = []
index_col = 2
for i in range(len(df.iloc[:,0])):
    if str(df.iloc[i, 0]) == 'nan':
        # 遇到空格了
        print('new_0:',len(new_col_0))
        print('new_1:', len(new_col_1))
        df.loc[0:998, index_col] = new_col_0
        df.loc[0:998, index_col+1] = new_col_1
        index_col += 2
        new_col_0 = []
        new_col_1 = []
        continue
    new_col_0.append(df.iloc[i, 0])
    new_col_1.append(df.iloc[i, 1])
# 删除多的行
df = df.drop(df.index[1000:])
df.to_excel('work_new.xlsx', index=False,header=False)
