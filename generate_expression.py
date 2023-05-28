import random


OPERATIONS = ['+', '-', '*', '/']

EXPRESSION_DEPTH = 3
POPULATION_SIZE = 10
INITIAL_FITNESS = 1000
GENERATION_SIZE = 10000


class Chromosome():
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.left} {self.op} {self.right})'


def evaluate_chromo(chromo):
    if isinstance(chromo, int):
        return chromo

    op = chromo.op
    left = evaluate_chromo(chromo.left)
    right = evaluate_chromo(chromo.right)

    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left / right
    else:
        return 0

def generate_chromo(depth):
    if depth <= 0:
        return random.randint(0, 10)

    op = random.choices(OPERATIONS, weights=None, k=1)[0]
    left = generate_chromo(depth - 1)
    right = generate_chromo(depth - 1)

    return Chromosome(op, left, right)

def generate_population(size):
    return list(map(lambda _: generate_chromo(EXPRESSION_DEPTH), range(size)))

def fitness(chromo, target):
    evaluation = evaluate_chromo(chromo)
    return abs(target - evaluation)

def mutate(chromo):
    op = chromo.op
    left = None
    right = None

    if random.randint(1, 100) > 50:
        left = generate_chromo(EXPRESSION_DEPTH - 1)
        right = chromo.right
    else:
        left = chromo.left
        right = generate_chromo(EXPRESSION_DEPTH - 1)

    return Chromosome(op, left, right)

def cross(chromo1, chromo2):
    op = chromo1.op if random.randint(1, 100) > 50 else chromo2.op
    left = chromo1.left if random.randint(1, 100) > 50 else chromo2.left
    right = chromo1.right if random.randint(1, 100) > 50 else chromo2.right

    return Chromosome(op, left, right)

def run(target):
    population = generate_population(POPULATION_SIZE)
    fitnesses = list(map(lambda _: 1000, range(POPULATION_SIZE)))
    best1 = best2 = 0
    worst1 = worst2 = 0

    for _ in range(GENERATION_SIZE):
        for i in range(POPULATION_SIZE):
            try:
                fitnesses[i] = fitness(population[i], target)
            except ZeroDivisionError:
                population[i] = generate_chromo(EXPRESSION_DEPTH)

        for i in range(POPULATION_SIZE):
            if fitnesses[i] < fitnesses[best1]:
                best2 = best1
                best1 = i

            if fitnesses[i] > fitnesses[worst1]:
                worst2 = worst1
                worst1 = i

        population[worst1] = mutate(population[best1])
        population[worst2] = cross(population[best1], population[best2])

    return population[best1]

if __name__ == '__main__':
    chromo = run(target=100)
    print('expression:', chromo)
    print('evaluation:', evaluate_chromo(chromo))
