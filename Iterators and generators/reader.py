def read_next(*args):
    for item in args:
        for el in item:
            yield el


for i in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(i, end='')