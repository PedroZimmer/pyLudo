class LudoPeca:
    def __init__(self, color):
        self.color = color
        self.position = 0

    def move(self, steps):
        self.position += steps

    def reset(self):
        self.position = 0