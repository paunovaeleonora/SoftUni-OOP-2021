class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError('You must add a number.')
        result = ''
        for current_char in self.text:
            char_number = ord(current_char) + other
            while char_number < 32:
                char_number += 95
            while char_number > 126:
                char_number -= 95
            result += chr(char_number)
        return result



some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))

example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))