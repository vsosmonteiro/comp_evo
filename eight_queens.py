import random


class Mycromo:
    def __init__(self, matrix):
        self.matrix = matrix


def createpop():
    for i in range(10):
        newCromo = Mycromo(matrix=[])
        for k in range(8):
            newCromo.matrix.append(randomline())
        pop.append(newCromo)


def crossing(cromo1, cromo2):
    crossed = Mycromo(matrix=[])
    for i in range(8):
        if random.randint(0, 100) > 50:
            crossed.matrix.append(cromo1.matrix[i])
        else:
            crossed.matrix.append(cromo2.matrix[i])
    return crossed


def randomline():
    newlist = [0, 0, 0, 0, 0, 0, 0, 0]
    newlist[random.randint(0, 7)] = 1
    return newlist


def mutate(mycromo):
    for i in range(8):
        for j in range(8):
            if random.randint(0, 100) > 50:
                mycromo.matrix[i] = randomline()
    return mycromo


def printpop():
    for i in range(10):
        for k in range(8):
            print(pop[i].matrix[k])
        print('end')


def fitness(cromo):
    fit = 0
    aux = 0
    for i in range(8):
        for j in range(8):
            if cromo.matrix[j][i] == 1:
                aux += 1
        if aux > 1:
            fit += aux
        aux = 0

    for i in range(8):
        for j in range(8):
            ihelp = i
            jhelp = j
            while ihelp < 8 and jhelp < 8:
                if cromo.matrix[ihelp][jhelp] == 1:
                    aux += 1
                jhelp += 1
                ihelp += 1
            if aux > 1:
                fit += aux
            aux = 0

            ihelp = i
            jhelp = j
            while ihelp > 0 and jhelp > 0:
                if cromo.matrix[ihelp][jhelp] == 1:
                    aux += 1
                jhelp -= 1
                ihelp -= 1
            if aux > 1:
                fit += aux
            aux = 0

            ihelp = i
            jhelp = j
            while ihelp > 0 and jhelp < 8:
                if cromo.matrix[ihelp][jhelp] == 1:
                    aux += 1
                jhelp += 1
                ihelp -= 1
            if aux > 1:
                fit += aux
            aux = 0

            ihelp = i
            jhelp = j
            while ihelp < 8 and jhelp > 0:
                if cromo.matrix[ihelp][jhelp] == 1:
                    aux += 1
                jhelp -= 1
                ihelp += 1
            if aux > 1:
                fit += aux
            aux = 0

    return fit


def printcromo(cromo):
    for i in range(8):
        print(cromo.matrix[i])


def improve():
    fit = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    max1 = 0
    max2 = 0
    worst1 = 0
    worst2 = 0
    while fit.count(0) == 0:
        for i in range(10):
            fit[i] = fitness(pop[i])
        if fit.count(0):
            break
        for k in range(10):
            if fit[k] < fit[max1]:
                max2 = max1
                max1 = k

            if fit[max2] > fit[k] > fit[max1]:
                max2 = k

            if fit[k] > fit[worst1]:
                worst2 = worst1
                worst1 = k

            if fit[worst2] < fit[k] < fit[worst1]:
                worst2 = k

        mutate1 = mutate(pop[max1])
        cross1 = crossing(pop[max1], pop[max2])

        pop[worst2] = cross1
        pop[worst1] = mutate1

    printcromo(pop[max1])


if __name__ == '__main__':
    pop = []
    createpop()

    improve()
