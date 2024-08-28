import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

# 定义高斯函数
def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))

# 读取数据
data = pd.read_csv('file_path', sep="\t")
x = data['Energy']
y = data['Counts']

# 进行拟合
popt, _ = curve_fit(gaussian, x, y)

# 打印拟合参数
print(popt)