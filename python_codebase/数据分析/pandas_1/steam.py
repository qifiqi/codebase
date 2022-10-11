import pandas as pd

steam = pd.read_csv('../爬虫爬到的数据/steam_discount.csv', skiprows=1)
print(steam.info())
print(steam.drop_duplicates('游戏名字', keep='last', inplace=True))
print(steam.head())
print(steam.info())
steam.to_csv('./sj/steam.csv')
