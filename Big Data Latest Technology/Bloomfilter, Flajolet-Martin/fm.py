import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm


class FM1:
    def __init__(self, domain_size):
        # self.bitarray = 0
        self.R = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size))
        self.mask = (1 << self.n_bits) - 1
        self.seed = random.randint(0, 9999999)

    def put(self, item):
        h = mmh3.hash(item, self.seed) & self.mask
        r = 0

        if h == 0:
            return

        while (h & (1 << r)) == 0:
            r += 1  # r은 첫번째 1에서 멈춤

        if self.R < r:
            self.R = r


        # self.bitarray |= (1 << r)

    def size(self):
        # r = 0

        # while (self.bitarray & (1 << R) != 0):
        #     R += 1

        return 2 ** self.R


class FM2:
    def __init__(self, domain_size):
        self.bitarray = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size))
        self.mask = (1 << self.n_bits) - 1
        self.seed = random.randint(0, 9999999)

    def put(self, item):
        h = mmh3.hash(item, self.seed) & self.mask
        r = 0

        if h == 0:
            return

        while (h & (1 << r)) == 0:
            r += 1  # r은 첫번째 1에서 멈춤

        self.bitarray |= (1 << r)

    def size(self):
        R = 0

        while (self.bitarray & (1 << R) != 0):
            R += 1

        return 2 ** R / 0.77351


fm1 = FM1(100000)
fm2 = FM2(100000)

tset = set()

x = []
y1 = []
y2 = []

for i in tqdm(range(100000)):
    item = str(random.randint(0, 10000))
    fm1.put(item)
    tset.add(item)
    fm2.put(item)

    x.append(len(tset))
    y1.append(fm1.size())
    y2.append(fm2.size())


    # print(f"true: {len(tset)}, estimated: {fm.size()}")

plt.figure(figsize=(15,8))
plt.scatter(x, y1, color = 'r', label = 'FM Version1')
plt.scatter(x, y2, color = 'b', label = 'FM Version2')
plt.plot(x, x, color = 'gray')
plt.title('Flajolet-Martin Version 1,2', fontsize=25)
plt.legend(fontsize = 15, loc = 'best')
plt.show()