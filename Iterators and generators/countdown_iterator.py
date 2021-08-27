class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        cur_num = self.count
        self.count -= 1
        return cur_num


iterat = countdown_iterator(10)
for i in iterat:
    print(i, end=' ')