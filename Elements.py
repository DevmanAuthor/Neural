from collections import Counter

List = {
    "Tin": "abc", 
    "Iron": "abcddd",
    "Steel": "zzxy"
    }


def evaluate_element(string):
    string.lower()
    return dict(Counter(string.replace(' ', '')))
 

def match_compound(compound, string):
    if compound == evaluate_element(string):
        return True
    else:
        return False


def generate_compounds(string):
    str_cnt = Counter(string)
    comp = ""
    for key, value in List.items():
        e_cnt = Counter(List[key])
        if (e_cnt & str_cnt) == e_cnt:
            comp += (key + ".")
    print(comp)


def break_down_compound(dictry):
    s = str()
    for key, val in dictry.items():
        s += str(key) * dictry[key]
    return s


def break_down_element(string):
    s = str()
    d = evaluate_element(string)
    d = break_down_compound(d)
    return d
