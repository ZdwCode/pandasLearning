import pandas as pd
import matplotlib.pyplot as plt
air_qualtiy = pd.read_csv('../datas/air_quality.csv', index_col=0, parse_dates=True)
print(air_qualtiy)
air_qualtiy.plot()
plt.show()
air_qualtiy['station_antwerp'].plot()
plt.show()
air_qualtiy.plot.scatter(x='station_london', y='station_paris',alpha=0.5)
plt.show()

for method_name in dir(air_qualtiy.plot):
    print(method_name)
air_qualtiy.plot.box()
plt.show()