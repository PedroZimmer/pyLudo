import random

class Dado:
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll(self):
        return random.choice(self.sides)
    
