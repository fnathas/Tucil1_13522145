import random

def randMatrix(elements: list, n: int, m: int):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.choice(elements))
        matrix.append(row)
    return matrix

def randSequences(elements: list, n: int, k: int):
    sequences = []
    for i in range(k):
        sequence = []
        for j in range(random.randint(2, n)):
            sequence.append(random.choice(elements))
        sequences.append(sequence)
    return sequences

def randRewards(k: int):
    rewards = []
    for i in range(k):
        rewards.append(random.randint(1, 100))
    return rewards