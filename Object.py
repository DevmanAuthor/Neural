Elemental = {"Integrity": 100}

Bodylimb = {"Integrity": 10, "Strength": 10, "Flexibility": 10, "Reflexiveness": 10}

Compounds = {"Metal": (3, 2, 1), "Wood": (2, 2, 2), "Organic": (9, 9, 0)}


def evaluate_dna(string):
    numa = numb = numc = 0
    for i in range(len(string)):
        if string[i] is 'A':
            numa += 1
        elif string[i] is 'B':
            numb += 1
        elif string[i] is 'C':
            numc += 1
    return (numa, numb, numc)


def determine_compound(compound, string):
    if tuple(compound) == evaluate_dna(string):
        return True
    else:
        return False


class Stats(dict):
    def __init__(self, args):
        self = args
