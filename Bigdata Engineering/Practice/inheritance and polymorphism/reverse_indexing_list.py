class ReverseIndexList(list):
    def __init__(self, list_obj):
        super().__init__(list_obj) # list(obj)

    def __getitem__(self, index):
        return super().__getitem__(len(self) - 1 - index)

a = list(range(5))
print(a[0], a[1], a[2], a[3], a[4])
b = ReverseIndexList(a)
print(b)
print(b[0], b[1], b[2], b[3], b[4])


"""class Node:
    def __init__(self, num):
        self.num = num
        self.List = [None] * num

    def __len__(self):
        return self.num

    def __contains__(self, target):
        self.count = 0
        for i in range(len(self.List)):
            if self.List[i] == target:
                return True

        return False


print(a.__contains__(None))
>> > True

print(None in a)
>> > True"""