class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.number:
            idx = self.current_index
            self.current_index += 1
            return self.sequence[idx % len(self.sequence)]
        else:
            raise StopIteration


res = sequence_repeat('abc', 1)
for item in res:
    print(item, end='')