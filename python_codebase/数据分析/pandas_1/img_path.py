import pandas as pd

img_shujv = pd.read_csv('../爬虫爬到的数据/img_src.csv')
print(img_shujv.drop_duplicates(inplace=True))
print(img_shujv.info())
print(img_shujv.reset_index(drop=True,inplace=True))
print(img_shujv.to_csv('../爬虫爬到的数据/img_清洗过.csv'))
