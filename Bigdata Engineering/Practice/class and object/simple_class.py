class PracticeClass:
    def __init__(self, att1, att2):
        self.att1 = att1
        self.att2 = att2

    def print_att1(self):
        print(self.att1)

    def print_att2(self):
        print(self.att2)

obj = PracticeClass(3, 'hihi')
obj.print_att1()
obj.print_att2()