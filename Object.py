Elemental = {"Integrity": 100}

Bodylimb = {"Strength": 10, "Flex": 10}

Compounds = {"Metal": (3, 2, 1), "Wood": (7, 0, 1), "Organic": (9, 9, 0)}


def evaluate_dna(strelement):
    numa = numb = numc = 0
    for i in range(len(strelement)):
        if strelement[i] is 'A':
            numa += 1
        elif strelement[i] is 'B':
            numb += 1
        elif strelement[i] is 'C':
            numc += 1
    return (numa, numb, numc)


def interpret_compound(compound, strelement):
    if tuple(compound) == evaluate_dna(strelement):
        return True
    else:
        return False


class Stats():
    def __init__(self, args):
        self = args
