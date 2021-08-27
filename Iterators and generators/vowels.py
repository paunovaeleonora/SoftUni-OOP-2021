class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.all_vowels = 'aeiouy'
        self.vowels = [el for el in self.text if el.lower() in self.all_vowels]
        self.end = len(self.vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current_i = self.start
        self.start += 1
        return self.vowels[current_i]

text = vowels('ajakadhnogei')
for el in text:
    print(el)

