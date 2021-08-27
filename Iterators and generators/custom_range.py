class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp


a = custom_range(1, 10)
for el in a: print(el)
