import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Reservoir:
    def __init__(self, k):
        self.sampled = []  # sampling 한 값들을 담을 리스트 생성
        self.k = k # 몇개를 샘플링 할지:k
        self.cnt = 0  # 현재까지 들어온 스트림이 몇번째 스트림인지
        # 현재 들어온 아이템이 몇번째로 들어온 아이템인지, 초기에는 들어온 값이 없으므로 0

    def put(self, item):  # 스트림에서 아이템이 들어왔을 때 어떻게 처리할 것인지
        if self.cnt < self.k: # 초기에 k개의 배열을 채우는 과정
            self.sampled.append(item)
        else:
            r = random.randint(0, self.cnt) # 0에서 self.cnt까지의 값을 리턴 // randrange()는 self.cnt-1까지
            if r < self.k:
                self.sampled[r] = item

        self.cnt += 1


class ReservoirWithReplacement:
    def __init__(self, k):
        self.k = k
        self.sampled = []
        self.total = []

    def put(self, item):
        self.total.append(item)
        self.sampled = [random.choice(self.total) for x in range(self.k)]


# 숫자의 등장횟수 저장하기 위한 사전생성
sample_dict = {key : value for key, value in zip(np.arange(1000), np.zeros(1000))}

for i in tqdm(range(10000)): # 10000회 반복
    reservoir_replacement = ReservoirWithReplacement(100) # 100개의 값을 추출하는 시행
    for j in range(1000): # 0 부터 999 까지의 숫자가 입력되는 스트림
        reservoir_replacement.put(j)
    for k in reservoir_replacement.sampled: # 숫자 등장시 횟수 증가
        sample_dict[k] += 1

plt.plot(sample_dict.keys(), sample_dict.values())
plt.xticks(np.arange(0, 1001, 100))
plt.xlabel("sampling number")
plt.ylabel("number of outputs")
plt.title("Reservoir Sampling with Replacement")
plt.savefig("Reservoir Sampling with Replacement.jpg")
plt.show()