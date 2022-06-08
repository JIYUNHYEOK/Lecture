import mmh3
import math
import random
import matplotlib.pyplot as plt
from tqdm import tqdm


class FM:
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


fm = FM(1000000)

tset = set()

x = []
y = []

for i in tqdm(range(1000000)):
    item = str(random.randint(0, 100000))
    fm.put(item)
    tset.add(item)

    x.append(len(tset))
    y.append(fm.size())


    # print(f"true: {len(tset)}, estimated: {fm.size()}")

plt.scatter(x,y)
plt.plot(x,x, color = 'r')
plt.show()