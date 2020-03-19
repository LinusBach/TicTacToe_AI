import tictactoe as t, random as r, net as n, matplotlib.pyplot as plt


class Simulation:

    net = n.Net()

    def simulate_graphics(self, trainings_gesamt, datenpunkte, precision, funct_p1, funct_p2):
        trainings = []
        for i in range(datenpunkte + 1):
            trainings.append(int(i*trainings_gesamt/datenpunkte))
        a = self.simulate_training(trainings, precision, funct_p1, funct_p2)
        results = a[0]
        error = a[1]
        plt.plot(trainings, results[0], label='Spieler 1 gewinnt')
        plt.plot(trainings, results[1], label='Unentschieden')
        plt.plot(trainings, results[2], label='Spieler 2 gewinnt')
        plt.axis([0, trainings_gesamt, 0, 100])
        plt.xlabel('Simulationsdurchläufe')
        plt.ylabel('Wahrscheinlichkeit in Prozent (%)')
        plt.title('Ergebnisse der Simulation')
        plt.legend()
        plt.show()
        plt.plot(error)
        plt.axis([90, trainings_gesamt, 0, 0.25])
        plt.xlabel('Trainingsdurchläufe')
        plt.ylabel('Fehler')
        plt.title('Fehler im Verlauf der Trainingsdurchläufe')
        plt.show()

    def simulate_training(self, trainings, games, funct_p1, funct_p2):
        trainings_overall = 0
        error = []
        results = [[], [], []]
        for training in trainings:
            for e in self.net.train(training - trainings_overall):
                error.append(e)
            trainings_overall = training
            result = self.simulate(games, funct_p1, funct_p2)
            results[0].append(round(result[0]/games*100, 2))
            results[1].append(round(result[1]/games*100, 2))
            results[2].append(round(result[2]/games*100, 2))
            print('after {} trainings:\nplayer 1 wins: {}% ({})\ndraws: {}% ({})\nplayer 2 wins: {}% ({})\n'.format(
                trainings_overall, round(result[0]/games*100, 2), result[0], round(result[1]/games*100, 2), result[1],
                round(result[2]/games*100, 2), result[2]))
        return [results, error]

    def simulate(self, games, funct_p1, funct_p2):
        results = [0, 0, 0]
        for i in range(games):
            results[self.simulate_game(funct_p1, funct_p2)+1] += 1
        return results

    def simulate_game(self, funct_p1, funct_p2):
        g = t.Game()
        run = True
        while run:

            # Zug Spieler 1
            funct_p1(g)
            if g.turn == 8 or g.winner != 0:
                break

            # Zug Spieler 2
            funct_p2(g)
            if g.turn == 8 or g.winner != 0:
                break

        # g.printgrid()
        return g.winner

    @staticmethod
    def play_rand(game, debug=False):
        while True:
            rand = r.randint(0, 8)
            if game.play(rand) >= 0:
                break
        if debug: print("r: " + str(rand))

    @staticmethod
    def play_human(game, debug=False):
        game.printgrid()
        while True:
            if game.play(int(input())) >= 0:
                break



s = Simulation()
results = s.simulate(100000, s.play_rand, s.play_rand)
for a in results:
    print(round(a/1000, 2))

# s.net.train(1000)
# s.simulate(5, s.net.play, s.play_rand)

# s.simulate_graphics(150, 50, 1000, s.net.play, s.play_rand)
