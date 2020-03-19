class Game:

    def __init__(self, silent=True):
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = -1
        self.turn = 0
        self.winner = 0
        self.silent = silent

    def play(self, spot):
        if self.field[spot] != 0:
            if not self.silent:
                print('incorrect input: spot occupied')
            return -1
        self.turn += 1
        self.field[spot] = 1
        if self.check():
            if not self.silent:
                print('player %d just won in turn %d' % (int(self.player/-2+1.5), self.turn))
            self.winner = self.player
            return 1
        elif self.turn >= 8:
            if not self.silent:
                print('draw, nobody won')
            return 1
        self.player *= (-1)
        self.invertfield()
        return 0

    def invertfield(self):
        for i in range(9):
            self.field[i] *= -1

    def printgrid(self):
        print("\n", self.field[:3], "\n", self.field[3:-3], "\n", self.field[-3:], "\n")

    def check(self):
        win = False
        for a in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.field[a[0]] == self.field[a[1]] == self.field[a[2]] != 0:
                win = True
        return win

    def clear(self):
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = -1
        self.turn = 0
        self.winner = 0
