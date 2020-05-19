from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('135789'))

def normalize(name: str):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(list):
    def mul(x, y):
        return x * y
    return reduce(mul, list)
print(prod([3, 5, 7, 9]))

def str2float(s):
    dot = False
    point = 1

    def char2num(s):
        nonlocal dot
        if s != '.':
            return digits[s]
        else:
            dot = True
            return -1

    def fun(x, y):
        nonlocal point
        print(y)
        if y == -1:
            return x
        if dot:
            point = point * 10
            return x + y / point
        else:
            return x * 10 + y
    return reduce(fun, map(char2num, s))

print(str2float('125.889'))