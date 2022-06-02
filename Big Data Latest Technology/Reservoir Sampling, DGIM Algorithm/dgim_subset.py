import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


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


# dgim_bits = DGIM_BITS()
dgim_subsetsum = DGIM_SUBSET()

data = []
data_sum = []
# dgim_bits_sum = []
dgim_subsetsum_sum = []

for i in tqdm(range(10000)):
    r = random.randint(0, 15)
    data.append(r)
#     dgim_bits.put(r)
    dgim_subsetsum.put(r)

# dgim_bits.stream()

for i in tqdm(range(1, 2001)):
    data_sum.append(sum(data[-i:]))
#     dgim_bits_sum.append(dgim_bits.sum_bits(i))
    dgim_subsetsum_sum.append(dgim_subsetsum.sum_subset(i))


plt.plot(np.arange(1, 2001), data_sum, linewidth=6, c='grey', label='data')
# plt.plot(np.arange(1, 2001), dgim_bits_sum, linestyle='dotted', linewidth=6, alpha=.5, c='red', markersize=5,
#          label='DGIM_bits')
plt.plot(np.arange(1,2001), dgim_subsetsum_sum, linestyle='dashed', linewidth=6, alpha=.5, c = 'blue', markersize=5, label = 'DGIM_subset')
plt.title("DGIM Algorithm used subsetsum", )
plt.xlabel('count of recent stream')
plt.ylabel("recent stream of k's sum")
plt.savefig("DGIM_subsetsum.jpg")
plt.legend(loc='best')
plt.show()