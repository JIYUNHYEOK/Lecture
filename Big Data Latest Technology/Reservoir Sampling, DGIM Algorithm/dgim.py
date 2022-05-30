import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class Bucket_BITS:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start},{self.end})"


class DGIM_BITS:
    def __init__(self):
        self.bucket_tower = [[[]], [[]], [[]], [[]]]  # 총 4개의 stream으로 구성
        self.num_bits = [[], [], [], []]  # 0 ~ 15는 4bits로 표현 가능
        self.ts = 0  # timestamp
        self.size = 0

    def put(self, num):
        for i in range(4):
            self.num_bits[i].append(int(format(num, '04b')[3 - i]))
        self.size += 1

    def stream(self):
        for i in range(len(self.num_bits)):
            self.ts = 0

            for j in range(len(self.num_bits[i])):
                if self.num_bits[i][j] == 1:
                    self.bucket_tower[i][0].insert(0, Bucket_BITS(self.ts, self.ts))
                    layer = 0

                    while len(self.bucket_tower[i][layer]) > 2:
                        if len(self.bucket_tower[i]) <= layer + 1:
                            self.bucket_tower[i].append([])

                        b1 = self.bucket_tower[i][layer].pop()
                        b2 = self.bucket_tower[i][layer].pop()
                        b1.end = b2.end

                        self.bucket_tower[i][layer + 1].insert(0, b1)
                        layer += 1

                self.ts += 1

    def sum_bits(self, k):
        total = 0
        s = self.size - k

        for digit, digit_value in enumerate(self.bucket_tower):
            sumofvalue = 0

            for layer, buckets in enumerate(digit_value):
                for bucket in buckets:
                    if s < bucket.start:
                        sumofvalue += (1 << layer)
                    elif s <= bucket.end:
                        sumofvalue += (1 << layer) * ((bucket.end - s + 1) / (bucket.end - bucket.start + 1))

            total += (1 << digit) * sumofvalue

        return total


class Bucket_SUBSET:
    def __init__(self, start, end, intervalsum):
        self.start = start
        self.end = end
        self.intervalsum = intervalsum

    def __repr__(self):
        return f"({self.start},{self.end},{self.intervalsum})"


class DGIM_SUBSET:
    def __init__(self):
        self.bucket_tower = [[]]
        self.ts = 0
        self.sumvalue = 0
        self.start = 0
        self.end = 0

    def put(self, num):
        self.bucket_tower[0].insert(0, Bucket_SUBSET(self.ts, self.ts, num))
        layer = 0

        while len(self.bucket_tower[layer]) > 2:
            self.start = 0
            self.end = 0
            self.sumvalue = 0

            if len(self.bucket_tower) <= layer + 1:
                self.bucket_tower.append([])

            self.start = self.bucket_tower[layer][-1].start

            while self.sumvalue <= (1 << (layer)):
                if len(self.bucket_tower[layer]) == 1:
                    break

                self.sumvalue += self.bucket_tower[layer][-1].intervalsum
                self.end = self.bucket_tower[layer][-1].end
                self.bucket_tower[layer].remove(self.bucket_tower[layer][-1])

            self.bucket_tower[layer + 1].insert(0, Bucket_SUBSET(self.start, self.end, self.sumvalue))

            layer += 1

        self.ts += 1

    def sum_subset(self, k):
        total = 0
        s = self.ts - k

        for buckets in self.bucket_tower:
            for bucket in buckets:
                if s < bucket.start:
                    total += bucket.intervalsum
                elif s <= bucket.end:
                    total += bucket.intervalsum * ((bucket.end - s + 1) / (bucket.end - bucket.start + 1))
                    return total
                else:
                    return total

        return total


dgim_bits = DGIM_BITS()
dgim_subsetsum = DGIM_SUBSET()

data = []
data_sum = []
dgim_bits_sum = []
dgim_subsetsum_sum = []

for i in tqdm(range(10000)):
    r = random.randint(0, 15)
    data.append(r)
    dgim_bits.put(r)
    dgim_subsetsum.put(r)

dgim_bits.stream()

for i in tqdm(range(1, 2001)):
    data_sum.append(sum(data[-i:]))
    dgim_bits_sum.append(dgim_bits.sum_bits(i))
    dgim_subsetsum_sum.append(dgim_subsetsum.sum_subset(i))

plt.plot(np.arange(1, 2001), data_sum, linewidth=6, c='grey', label='data')
plt.plot(np.arange(1, 2001), dgim_bits_sum, linestyle='dotted', linewidth=6, c='red', markersize=5,
         label='DGIM_bits')
plt.plot(np.arange(1,2001), dgim_subsetsum_sum, linestyle='dashed', linewidth=6, alpha=.5, c = 'blue', markersize=5, label = 'DGIM_subset')
plt.title("DGIM Algorithm", )
plt.xlabel('count of recent stream')
plt.ylabel("recent stream of k's sum")
plt.savefig("DGIM.jpg")
plt.legend(loc='best')
plt.show()

dgim_bits_diff = [(i-j) for i, j in zip(data_sum, dgim_bits_sum)]
dgim_subsetsum_diff = [(i-j) for i, j in zip(data_sum, dgim_subsetsum_sum)]

plt.plot(np.arange(1, 2001), dgim_bits_diff, linewidth=2, c='grey', label='dgim_bits_diff')
plt.plot(np.arange(1, 2001), dgim_subsetsum_diff, linewidth=2, c='blue', label='dgim_subset_diff')
plt.title("DGIM Algorithm Error")
plt.xlabel('count of recent stream')
plt.ylabel("recent stream of k's sum")
plt.savefig("DGIM_diff.jpg")
plt.legend(loc='best')
plt.show()

# np.mean(dgim_bits_diff), np.mean(dgim_subsetsum_diff)