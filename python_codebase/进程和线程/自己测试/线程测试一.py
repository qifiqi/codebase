import threading


def aa(name, num):
    for i in range(num):
        print("%s：输出%d" % (name, i))


n = threading.Thread(target=aa, args=('a', 100))
m = threading.Thread(target=aa, args=('b', 100))
n.start()
m.start()
# n.join()
print('结束'*88)



