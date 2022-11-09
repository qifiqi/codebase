import json
import os
import pprint
import sys

from core.content import get_Data
from concurrent.futures import ThreadPoolExecutor
from core import login_hodj
threa = ThreadPoolExecutor(max_workers=32)

sys.path.append(os.getcwd())


def get_list(data):
    # param = {"no": "dy0002", "data": {"days": 1, "rankType": 5, "liveDay": f"2022-{months.zfill(2)}-{day.zfill(2)}"}}
    param = {"no": "dy3026", "data": {"ankType": "音乐原创榜","rankDay": f"{data}"}}
    aa = get_Data(param)
    pprint.pp(aa)
    with open(f'static/json_file_dir/{param.get("no")}_{param.get("data").get("liveDay")}.json', 'a+',
              encoding='utf-8') as f:
        f.write(json.dumps(aa))
        f.close()


if __name__ == '__main__':
    # months = input("输入你想要的月份")
    # day = input("输入你要的天数")
    data_time = []
    login_hodj.get_log()
    for i in range(1, 13):
        if i == 2:
            for j in range(1, 28 + 1):
                data_time.append(f"2021-{str(i).zfill(2)}-{str(j).zfill(2)}")

        elif i in [1, 3, 5, 7, 8, 10, 12]:
            for j in range(1, 32):
                data_time.append(f"2021-{str(i).zfill(2)}-{str(j).zfill(2)}")

        elif i in [4, 6, 9, 11]:
            for j in range(1, 31):
                data_time.append(f"2021-{str(i).zfill(2)}-{str(j).zfill(2)}")

    threa.map(get_list, data_time)
