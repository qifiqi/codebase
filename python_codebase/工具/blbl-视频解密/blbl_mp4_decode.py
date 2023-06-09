import sys
import os
from pathlib import Path
from numpy import fromfile, uint8   # pip install numpy

ROOT = Path(sys.argv[0]).resolve().parent  # 脚本文件的父文件夹的绝对路径
# 创建一个文件夹来存放
root_dir = os.path.basename(ROOT)
if not os.path.exists(os.path.basename(ROOT)):
    os.mkdir(os.path.basename(ROOT))

for f in ROOT.rglob("**/*.mp4"):
    read = fromfile(f, dtype=uint8)
    if all(read[0:3] == [255, 255, 255]):
        outfile = f"./{root_dir}/{str(f.name)}.mp4"
        read[3:].tofile(outfile)
        print(outfile)
