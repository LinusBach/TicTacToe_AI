import neuron as n, pickle, random as r


class Net:

    layer = [n.Neuron(9), n.Neuron(9), n.Neuron(9), n.Neuron(9), n.Neuron(9),
             n.Neuron(9), n.Neuron(9), n.Neuron(9), n.Neuron(9)]
    debug = False

    def __init__(self, debug=False):
        self.debug = debug

    def save(self):
        f = open("net.txt", 'r+b')
        pickle.Pickler(f, 0).dump(self.layer)
        f.close()

    def load(self, path="net.txt"):
        f = open(path, 'rb')
        self.layer = pickle.Unpickler(f).load()
        f.close()

    def train(self, trainings, batch_size=-1):
        f = open("training_data.txt", 'rb')
        data = pickle.Unpickler(f).load()
        f.close()
        if batch_size == -1:
            batch_size = data.__len__()
        error = []
        for i in range(trainings):
            batch_error = 0
            r.shuffle(data)
            batch = data[:batch_size]
            for a in batch:
                solution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                solution[a[1]] = 1
                for iLayer in range(9):
                    batch_error += self.layer[iLayer].learn(a[0], solution[iLayer])
            batch_error /= batch.__len__() * 9
            error.append(abs(batch_error))
        return error

    def play(self, game):
        results = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for iLayer in range(9):        # Berechnung der Ergebnisse spot für spot
            results[iLayer] = n.Neuron.sigmoid(self.layer[iLayer].think(game.field))
        choice = results.index(max(results))    # Filtern der Ergebnisse nach dem höchsten Wert
        while game.play(choice) < 0:               # Spielen der Entscheidung
            results[choice] = -1                # Anpassung, falls das Feld bereits besetzt ist
            choice = results.index(max(results))
        if self.debug: print("p: " + str(choice))
