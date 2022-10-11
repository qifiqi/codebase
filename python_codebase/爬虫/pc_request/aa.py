import pandas as pd
import pymysql as pm

steam = pd.read_csv('./steam_discount.csv', skiprows=1)
conn = pm.connect(user='root', db='book_db', password='123456', port=3306, host='localhost')
cursor = conn.cursor()
aa = 1
for i in steam.values:
    cursor.execute("INSERT INTO steam VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s')" %
                   (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    print(aa)
    aa += 1
else:
    conn.commit()
    cursor.close()
    conn.close()
