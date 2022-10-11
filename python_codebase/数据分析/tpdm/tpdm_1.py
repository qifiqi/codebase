import time
from tqdm import tqdm
from tqdm._tqdm import trange
#
for i in tqdm(range(100)):
    time.sleep(0.0001)


for j in trange(100):
    time.sleep(0.1)
# alist = list('letters')
# bar = tqdm(alist)
# for letter in bar:
#     bar.set_description(f"Now get {letter}")
# pbar = tqdm(["a", "b", "c", "d"])
# for char in pbar:
#     time.sleep(1)
#     pbar.set_description("Processing %s" % char)
