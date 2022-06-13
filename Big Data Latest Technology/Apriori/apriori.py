from itertools import combinations


# C2
def make_candidate(freq_itemsets, k):
    candidates = set()
    for itemset1 in freq_itemsets:
        for itemset2 in freq_itemsets:
            union = itemset1 | itemset2
            if len(union) == k:
                for item in union: # 각각의 부분집합이 freq_itemsets에 포함되는지 확인
                    if union - {item} not in freq_itemsets:
                        break
                else:
                    candidates.add(union)

    return candidates


# 일반화
def filter(candidates, k, s):
    itemset_cnt_k = {}
    with open("../data/groceries.csv", "r") as f:
        for line in f:
            basket = line.strip().split(",")
            for comb in combinations(basket, k):
                comb = frozenset(comb)
                if comb in candidates:
                    if comb not in itemset_cnt_k:
                        itemset_cnt_k[comb] = 0
                    itemset_cnt_k[comb] += 1

    freq_itemsets = set(itemset for itemset, cnt in itemset_cnt_k.items() if cnt >= s)

    return freq_itemsets


# item 갯수 구하기
s = 100

item_cnt = {}

with open("../data/groceries.csv", "r") as f:
    for line in f:
        basket = line.strip().split(",")
        for item in basket:
            if item not in item_cnt:
                item_cnt[item] = 0
            item_cnt[item] += 1


# L1
freq_itemsets = set(frozenset([item]) for item, cnt in item_cnt.items() if cnt >= s)

freq_itemsets_all = freq_itemsets.copy()

k = 2

while len(freq_itemsets) > 0:
    candidates = make_candidate(freq_itemsets, k)
    freq_itemsets = filter(candidates, k, s)
    freq_itemsets_all |= freq_itemsets
    # print(k, len(candidates), len(freq_itemsets))
    k += 1

# for fi in freq_itemsets_all:
#     print(fi)

lst = []

with open("../data/groceries.csv", "r") as f:
    for line in f:
        basket = line.strip().split(",")
        lst.append(basket)

dict_item_cnt = {}

for fi in freq_itemsets_all:
    for i in range(1, len(fi) + 1):
        for comb in combinations(fi, i):
            comb = sorted(list(comb))
            if tuple(comb) in dict_item_cnt:
                continue
            for basket in lst:
                cnt = 0
                size = len(comb)
                for element in comb:
                    if element in basket:
                        cnt += 1
                if cnt == size:
                    comb = tuple(list(comb))
                    if comb not in dict_item_cnt:
                        dict_item_cnt[comb] = 1
                    else:
                        dict_item_cnt[comb] += 1

# for key, value in dict_item_cnt.items():
#     print(key, value)

case = set()
c = 0.5

for fi in freq_itemsets_all:
    for i in range(1, len(fi)):
        for comb1 in combinations(fi, i):
            antecedent = tuple(sorted(list(comb1)))
            diff = fi.difference(antecedent)
            for j in range(1, len(diff) + 1):
                for comb2 in combinations(diff, j):
                    consequent = tuple(sorted(list(comb2)))
                    union = tuple(sorted(list(set(list(antecedent) + list(consequent)))))
                    conf = dict_item_cnt[union] / dict_item_cnt[antecedent]
                    if conf >= c:
                        case.add((antecedent, '->', consequent, conf))

for item in case:
    print(item)

print(len(case))