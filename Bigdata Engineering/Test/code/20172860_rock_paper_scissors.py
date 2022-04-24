import random


class Player:
    def __init__(self):
        self.num_wins = 0
        self.hand = ""

    def play(self):
        index = random.randint(1,3)
        if index == 1:
            self.hand = 'rock'
        elif index == 2:
            self.hand = 'paper'
        elif index == 3:
            self.hand = 'scissors'



    def feedback(self, opponent):
        if self.hand == opponent.hand:
            return 'draw'

        if self.hand == 'rock':
            if opponent.hand == 'paper':
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'
        elif self.hand == 'paper':
            if opponent.hand == 'scissors':
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'
        else:
            if opponent.hand == 'rock':
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'

me = Player()
opponent = Player()

for i in range(5):
    me.play()
    opponent.play()
    my_result = me.feedback(opponent)
    print(f"round-{i}, (me) {me.hand} vs {opponent.hand} (opponent)")
    print(f"round-{i}, {my_result}")