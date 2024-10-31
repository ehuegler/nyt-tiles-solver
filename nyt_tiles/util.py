from random import Random

def pop_random(lst: list, rng: Random):
    idx = rng.randint(0, len(lst) - 1)
    return lst.pop(idx)