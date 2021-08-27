def reverse_text(string):
    start = len(string) - 1

    while start >= 0:
        yield string[start]
        start -= 1

for char in reverse_text('step'):
    print(char, end='')