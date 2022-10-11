import json
import os
import pprint
import sys

from core.content import get_Data

sys.path.append(os.getcwd())

if __name__ == '__main__':
    months = input("输入你想要的月份")
    day = input("输入你要的天数")
    param = {"no": "dy0002", "data": {"days": 1, "rankType": 5, "liveDay": f"2022-{months.zfill(2)}-{day.zfill(2)}"}}
    aa = get_Data(param)
    pprint.pp(aa)
    with open(f'static/json_file_dir/{param.get("no")}_{param.get("data").get("liveDay")}.json','w',encoding='utf-8') as f:
        f.write(json.dumps(aa))
        f.close()


