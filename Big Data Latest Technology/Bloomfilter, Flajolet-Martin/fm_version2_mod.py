import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np


class FM:
    def __init__(self, domain_size, n_hash, group_size):
        self.domain_size = domain_size
        self.n_hash = n_hash
        self.bitarray = [0] * self.n_hash
        self.group_size = group_size
        self.n_bits = math.ceil(math.log2(domain_size))
        self.mask = (1 << self.n_bits) - 1
        self.seed = [random.randint(0, 9999999) for _ in range(self.n_hash)]


    def put(self, item):

        for i in range(self.n_hash):
            r = 0
            h = mmh3.hash(item, self.seed[i]) & self.mask

            if h == 0:
                return

            while (h & (1 << r)) == 0:
                r += 1  # r은 첫번째 1에서 멈춤

            self.bitarray[i] |= (1 << r)


    def size(self):
        rs = []
        for i in self.bitarray:
            R = 0
            while (i & (1 << R) != 0):
                R += 1
            rs.append(2 ** R / 0.77351)

        group = []

        for i in range(self.group_size):
            if i != self.group_size-1:
                # group[i] = rs[i*(len(rs)//self.group_size):(i+1)*(len(rs)//self.group_size)]
                group.append(rs[i * (len(rs) // self.group_size):(i + 1) * (len(rs) // self.group_size)])
            else:
                # group[i] = rs[i*(len(rs)//self.group_size):]
                group.append(rs[i * (len(rs) // self.group_size):])

        return np.mean([np.median(g) for g in group])


domain_size = 100000

fm1 = FM(domain_size, 100, 5)
fm2 = FM(domain_size, 100, 10)
fm3 = FM(domain_size, 100, 20)

fm4 = FM(domain_size, 100, 10)
fm5 = FM(domain_size, 200, 10)
fm6 = FM(domain_size, 500, 10)

tset = set()

x = []

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for i in tqdm(range(domain_size)):  # 100000
    item = str(random.randint(0, 10000))
    fm1.put(item)
    fm2.put(item)
    fm3.put(item)
    fm4.put(item)
    fm5.put(item)
    fm6.put(item)

    tset.add(item)

    x.append(len(tset))
    y1.append(fm1.size())
    y2.append(fm2.size())
    y3.append(fm3.size())
    y4.append(fm4.size())
    y5.append(fm5.size())
    y6.append(fm6.size())

    # print(f"true: {len(tset)}, estimated: {fm.size()}")


plt.figure(figsize=(15,8))
plt.subplot(2, 2, 1)
plt.scatter(x,y1, color = 'r', label = 'n_hash = 100, group = 5')
plt.scatter(x,y2, color = 'g', label = 'n_hash = 100, group = 10')
plt.scatter(x,y3, color = 'b', label = 'n_hash = 100, group = 20')
plt.plot(x,x, color = 'gray')
plt.title('Flajolet-Martin different group size', fontsize=25)
plt.legend(fontsize=15, loc = 'best')

plt.subplot(2, 2, 2)
plt.scatter(x,y4, color = 'r', label = 'n_hash = 100, group = 10')
plt.scatter(x,y5, color = 'g', label = 'n_hash = 200, group = 10')
plt.scatter(x,y6, color = 'b', label = 'n_hash = 500, group = 10')
plt.plot(x,x, color = 'gray')
plt.title('Flajolet-Martin different n_hash', fontsize=25)
plt.legend(fontsize=15, loc = 'best')
plt.show()