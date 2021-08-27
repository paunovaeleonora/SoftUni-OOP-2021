from itertools import permutations


def possible_permutations(data):
    permut = permutations(data)
    for i in permut:
        yield list(i)


for n in possible_permutations([1, 2, 3]):
    print(n)