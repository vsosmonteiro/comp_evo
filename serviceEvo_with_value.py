import random
import numpy as np

MUTATE_RATE = 0.2


class Cromossomo:
    def __init__(self, voice_gsm, voice_wcdma, data_gsm, data_wcdma):
        self.voice_gsm = voice_gsm
        self.voice_wcdma = voice_wcdma
        self.data_gsm = data_gsm
        self.data_wcdma = data_wcdma


def createPop(pop):
    for i in range(10):
        pop.append(mutateCromo((Cromossomo(10, 10, 10, 10))))


def fitness(cromo):
    cost_gsm = np.power(-30 + cromo.data_gsm + 0.24 * cromo.voice_gsm, 2)
    cost_wcdma = np.power(-80 + cromo.data_wcdma + 0.53 * cromo.voice_wcdma, 2)
    sum_voice = 1 - ((cromo.voice_wcdma + cromo.voice_gsm) / 275)
    sum_data = 1 - ((cromo.data_gsm + cromo.data_wcdma) / 110)
    return (cost_gsm + cost_wcdma) * sum_data * sum_voice


def mutateCromo(cromo):
    mycromo = cromo
    if random.randint(0, 100) > 50:
        mycromo.voice_gsm = random.randint(int(cromo.voice_gsm - cromo.voice_gsm * MUTATE_RATE), 125)
    if random.randint(0, 100) > 50:
        mycromo.voice_wcdma = random.randint(int(cromo.voice_wcdma - cromo.voice_wcdma * MUTATE_RATE), 150)
    if random.randint(0, 100) > 50:
        mycromo.data_gsm = random.randint(int(cromo.data_gsm * (1 - MUTATE_RATE)), 30)
    if random.randint(0, 100) > 50:
        mycromo.data_wcdma = random.randint(int(cromo.data_wcdma * (1 - MUTATE_RATE)), 80)

    return mycromo


def improve(pop):
    fit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    max1 = 0
    max2 = 0
    worst1 = 0
    worst2 = 0
    for i in range(1000):
        for j in range(10):
            fit[j] = fitness(pop[j])
        for k in range(10):
            if fit[k] < fit[max1]:
                max2 = max1
                max1 = k

            if fit[max2] > fit[k] > fit[max1]:
                max2 = k

            if fit[k] > fit[worst1]:
                worst2 = max1
                worst1 = k

            if fit[worst2] < fit[k] < fit[worst1]:
                worst2 = k

        mutate1 = mutateCromo(pop[max1])

        cross1 = cross(pop[max1], pop[max2])
        pop[worst2] = cross1
        pop[worst1] = mutate1

    print(pop[max1].voice_gsm)
    print(pop[max1].voice_wcdma)
    print(pop[max1].data_gsm)
    print(pop[max1].data_wcdma)
    print(fit[max1])
    print(max1)
    for i in range(10):
        print(fit[i])
    return pop


def cross(cromo1, cromo2):
    mycromo = Cromossomo(0, 0, 0, 0)
    if random.randint(0, 100) > 50:
        mycromo.voice_gsm = cromo1.voice_gsm
    else:
        mycromo.voice_gsm = cromo2.voice_gsm

    if random.randint(0, 100) > 50:
        mycromo.voice_wcdma = cromo1.voice_wcdma
    else:
        mycromo.voice_wcdma = cromo2.voice_wcdma

    if random.randint(0, 100) > 50:
        mycromo.data_gsm = cromo1.data_gsm
    else:
        mycromo.data_gsm = cromo2.data_gsm

    if random.randint(0, 100) > 50:
        mycromo.data_wcdma = cromo1.data_wcdma
    else:
        mycromo.data_wcdma = cromo2.data_wcdma

    return mycromo


if __name__ == '__main__':
    pop = []
    createPop(pop)
    improve(pop)
