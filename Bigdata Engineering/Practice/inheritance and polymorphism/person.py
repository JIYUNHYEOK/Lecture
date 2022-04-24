class Person:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "Person (%d)" %self.age

    def __lt__(self, other_person):
        return self.age < other_person.age

    def __le__(self, other_person):
        return self.age <= other_person.age

    def __gt__(self, other_person):
        return self.age > other_person.age

    def __ge__(self, other_person):
        return self.age >= other_person.age

    def __eq__(self, other_person):
        return self.age == other_person.age

    def __ne__(self, other_person):
        return self.age != other_person.age


a = Person(32)
b = Person(15)
c = Person(32)
d = Person(42)

person_list = [a, b, c, d]
person_list.sort()

for p in person_list:
    print(p)