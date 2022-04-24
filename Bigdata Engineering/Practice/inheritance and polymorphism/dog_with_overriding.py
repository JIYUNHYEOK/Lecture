class Dog:
    def __init__(self, name, weight, happiness, hunger):
        self._name = name
        self._weight = weight
        self._happiness = happiness
        self._hunger = hunger

    def play(self):
        print("%s is playing~" %self._name)
        print("happiness + 1 ==> %d" %self._happiness)
        self._happiness += 1

    def eat(self):
        print("%s is eating~" % self._name)
        print("hunger - 1 ==> %d" % self._hunger)
        self._hunger -= 1

    def bark(self):
        print('walwal')


class Husky(Dog):
    def __init__(self, name, weight, happiness, hunger):
        super().__init__(name, weight, happiness, hunger)

    def bark(self):
        print('grrrr')


class Terrier(Dog):
    def __init__(self, name, weight, happiness, hunger):
        super().__init__(name, weight, happiness, hunger)

    def bark(self):
        print('bowwow')


dogs = []
dogs.append(Dog("unknown", weight=15, happiness=1, hunger=10))
dogs.append(Terrier("Sam", weight=10, happiness=3, hunger=8))
dogs.append((Husky("Ellie", weight=20, happiness=5, hunger=4)))

for dog in dogs:
    dog.bark()