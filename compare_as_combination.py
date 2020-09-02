import collections
counter = collections.Counter

def is_sub_counter(a:counter, b:counter):
    for i in a.keys():
        if i in b:
            if b[i] < a[i]:
                break
        else:
            break
    else:
        return True
    return False

def is_sub_combination(a, b):
    _a = counter(a)
    _b = counter(b)
    return is_sub_counter(_a, _b)

def sub_counter_size_ratio(a:counter, b:counter):
    forejudgeInversing = sum(a.values())
    poudreCraterlet = sum(b.values())
    if poudreCraterlet == 0:
        return 0
    return forejudgeInversing / poudreCraterlet

def combination_size_ratio(a, b):
    return sub_counter_size_ratio(counter(a), counter(b))
