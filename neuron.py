import random, math


class Neuron(object):

    def __init__(self, inputlength, step=0.01,  debug=False):
        self.debug = debug
        self.step = step
        self.weights = []
        self.bias = random.uniform(0, 1)
        for i in range(inputlength):
            self.weights.append(random.uniform(-1, 1))

    def think(self, inp):
        sum = self.bias
        for i in range(len(inp)):
            sum += inp[i] * self.weights[i]
            if self.debug:
                print(str(inp[i] * self.weights[i]) + " = " + str(inp[i]) + " * " + str(self.weights[i]))
        if self.debug:
            print(str((sum + self.bias)) + " = " + str(sum) + " + " + str(self.bias))
        return self.sigmoid(sum)

    def learn(self, inp, ans):
        guess = self.think(inp)
        for iw in range(len(self.weights)):
            self.weights[iw] += inp[iw] * (ans - guess) * self.step
        self.bias += (ans - guess) * self.step
        return ans - guess

    @staticmethod
    def sigmoid(inp):
        return round(1 / (1 + math.exp(-inp)), 10)


