import math
import mmh3
import random

class BloomFilter:
    def __init__(self, capacity, fp_prob):
        # capacity = m (집합 S의 최대크기)
        # fp_prob = the ratio of False Positive
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.bitarray = 0
        self.n_bits = math.ceil(-math.log(fp_prob, math.e) * capacity / (math.log(2,math.e) **2))
        self.n_hashs = int(self.n_bits / capacity * math.log(2, math.e))
        self.seeds = [random.randint(0,999999) for i in range(self.n_hashs)]
        print(self.n_bits)
        print(self.n_hashs)

    def put(self, item):

        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits
            self.bitarray |= (1 << pos)


    def test(self, item):

        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits

            if self.bitarray & (1 << pos) == 0:
                return False

        return True


bloom = BloomFilter(10000, 0.1)

for i in range(1, 10001):
    bloom.put(str(i))

false_positive = []
cnt = 0
for i in range(1, 20001):

    if i <= 10000:
        print(f'{i} True', bloom.test(str(i)))
    else:
        cnt += 1
        print(f'{i} False', bloom.test(str(i)))
        if bloom.test(str(i)) == True:
            false_positive.append(str(i))

print(len(false_positive)/cnt)

# bloom.put('a')
# bloom.put('b')
# bloom.put('c')
# bloom.put('d')
# bloom.put('e')
#
# print('a', bloom.test('a'))
# print('b', bloom.test('b'))
# print('c', bloom.test('c'))
# print('d', bloom.test('d'))
# print('e', bloom.test('e'))
# print('f', bloom.test('f'))
# print('g', bloom.test('g'))
# print('h', bloom.test('h'))
# print('i', bloom.test('i'))
# print('j', bloom.test('j'))
# print('k', bloom.test('k'))
# print('l', bloom.test('l'))
# print('m', bloom.test('m'))
# print('n', bloom.test('n'))