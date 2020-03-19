import pickle, tictactoe as t, random as r

PATH = "training_data.txt"


def save(data):
    f = open(PATH, 'r+b')
    pickle.Pickler(f, 0).dump(data)
    f.close()


def load(path=PATH):
    f = open(path, 'rb')
    data = pickle.Unpickler(f).load()
    f.close()
    return data


def print_arr(a):
    for i in a: print(i)


def randomtraining(beginn=False):
    training = []
    g = t.Game()
    while True:
        inp = input()
        if not inp:
            break
        training.append([g.field[:], int(inp)])
        print(training[-1])
        if g.play(int(inp)) == 1:
            g.clear()
        g.printgrid()
        while True:
            rand = r.randint(0, 8)
            if g.play(rand) < 0:
                print(rand)
            else:
                break
        g.printgrid()

    return training

def randomtraining2(beginn=False):
    training = []
    g = t.Game()
    while True:
            rand = r.randint(0, 8)
            if g.play(rand) >= 0:
                break
    g.printgrid()
    while True:
            rand = r.randint(0, 8)
            if g.play(rand) >= 0:
                break
    g.printgrid()
    while True:
        inp = input()
        if not inp:
            break
        training.append([g.field[:], int(inp)])
        print(training[-1])
        if g.play(int(inp)) == 1:
            g.clear()
        g.printgrid()
        while True:
            rand = r.randint(0, 8)
            if g.play(rand) < 0:
                print(rand)
            else:
                break
        g.printgrid()

    return training


# new_data = randomtraining2()
# print_arr(new_data)
# print('\n')
# data = load()
# for a in new_data:
#     new = True
#     for b in data:
#         if a[0] == b[0]:
#             new = False
#             break
#     if new:
#         data.append(a)
#         print("Adding " + str(a) + " to dataset")
# print_arr(data)
# if input() == "y":
#     save(data)

data = load()
for a in data:
    print(str(data.index(a)) + ": " + str(a))
