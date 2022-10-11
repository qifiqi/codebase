from matplotlib import pyplot as plt

x = [22, 33, 44, 55, 33]
y = ['asdf ', 'as df', 'asd f', 'asdf ', 'asdfa ']

fig = plt.figure(figsize=(12, 8), dpi=80)
sub = fig.add_subplot(111)

sub.pie(x, explode=[0, 0, 0.1, 0, 0], labels=y)
plt.legend()
plt.show()
