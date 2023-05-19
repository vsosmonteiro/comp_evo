import random


class Cromossomo:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


def fill(mycromo, maxsize):
    while len(mycromo.a1) < maxsize:
        mycromo.a1.append('0')
    while len(mycromo.a2) < maxsize:
        mycromo.a2.append('0')
    while len(mycromo.a3) < maxsize:
        mycromo.a3.append('0')
    return mycromo


def mutate(mycromo):
    cromocopy = Cromossomo(mycromo.a1.copy(), mycromo.a2.copy(), mycromo.a3.copy())
    if cromocopy.a1.count('0') > 0:
        i = len(cromocopy.a1) - 1
        while i > 0:
            if cromocopy.a1[i] == '0':
                if random.randint(0, 100) > 50:
                    cromocopy.a1.pop(i)
                    cromocopy.a1.insert(random.randint(0, len(cromocopy.a1)), '0')

            i -= 1

    if cromocopy.a2.count('0') > 0:
        i = len(cromocopy.a2) - 1
        while i > 0:
            if cromocopy.a2[i] == '0':
                if random.randint(0, 100) > 50:
                    cromocopy.a2.pop(i)
                    cromocopy.a2.insert(random.randint(0, len(cromocopy.a2)), '0')

            i -= 1
    if cromocopy.a3.count('0') > 0:
        i = len(cromocopy.a3) - 1
        while i > 0:
            if cromocopy.a3[i] == '0':
                if random.randint(0, 100) > 50:
                    cromocopy.a3.pop(i)
                    cromocopy.a3.insert(random.randint(0, len(cromocopy.a3)), '0')

            i -= 1
    return cromocopy


def create_pop(entrada, maxsize):
    matrix = []
    for i in range(10):
        matrix.append(mutate(fill(Cromossomo(list(entrada[0]), list(entrada[1]), list(entrada[2])), maxsize)))
    return matrix


def cross(mycromo1, mycromo2):
    array1 = []
    array2 = []
    array3 = []
    for i in range(3):
        if random.randint(0, 100) > 50:
            array1 = mycromo1.a1
        else:
            array1 = mycromo2.a1
        if random.randint(0, 100) > 50:
            array2 = mycromo1.a2
        else:
            array2 = mycromo2.a2
        if random.randint(0, 100) > 50:
            array3 = mycromo1.a3
        else:
            array3 = mycromo2.a3
    return Cromossomo(array1, array2, array3)


def fitness(mycromo):
    valor = 0
    for i in range(maxsize):
        if mycromo.a1[i] != '0':
            if mycromo.a1[i] == mycromo.a2[i]:
                valor += 1
            else:
                if mycromo.a2 != '0':
                    valor -= 1

            if mycromo.a1[i] == mycromo.a3[i]:
                valor += 1
            else:
                if mycromo.a3[i] != '0':
                    valor -= 1

        if mycromo.a3[i] != '0':
            if mycromo.a3[i] == mycromo.a2[i]:
                valor += 1
            else:
                if mycromo.a2[i] != '0':
                    valor -= 1
    return valor


def read_entry(entradas):
    with open('my_input.txt', 'r') as file:
        for line in file:
            entradas.append(line.strip())


def improve():
    fit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    max1 = 0
    max2 = 0
    worst1 = 0
    worst2 = 0
    for i in range(100000):
        for j in range(10):
            fit[j] = fitness(pop[j])

        for k in range(10):
            if fit[k] > fit[max1]:
                print(fit[k])
                max2 = max1
                max1 = k
                if fit[k] == 10:
                    flag = True

            if fit[max2] < fit[k] < fit[max1]:
                max2 = k

            if fit[k] < fit[worst1]:
                worst2 = max1
                worst1 = k

            if fit[worst2] > fit[k] > fit[worst1]:
                worst2 = k

        mutate1 = mutate(pop[max1])

        cross1 = cross(pop[max1], pop[max2])
        pop[worst2] = cross1
        pop[worst1] = mutate1

    print(pop[max1].a1)
    print(pop[max1].a2)
    print(pop[max1].a3)
    print(fit[max1])
    return pop


if __name__ == '__main__':
    entradas = []
    maxsize = 0
    read_entry(entradas)
    for i in range(3):
        if len(entradas[i]) > maxsize:
            maxsize = len(entradas[i])
    pop = create_pop(entradas, maxsize)

    improve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
