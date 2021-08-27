class dictionary_iter:
    def __init__(self, dictionary):
        self.my_dict = list(dictionary.items())
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self.my_dict):
            curr_ind = self.start
            self.start += 1
            return self.my_dict[curr_ind]
        else:
            raise StopIteration


result = dictionary_iter({1: '1', 2: '2'})
for x in result:
    print(x)