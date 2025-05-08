class StringIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    Tags: iterator
    """

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.letter = ""
        self.letter_counter = 0

    def _get_next_letter(self):
        if self.letter_counter:
            self.letter_counter -= 1
            return self.letter

        self.letter = self.text[self.index]
        self.index += 1

        while (self.index < len(self.text) and
               self.text[self.index].isdigit()):
            self.letter_counter = 10 * self.letter_counter + int(self.text[self.index])
            self.index += 1

        if self.letter_counter:
            self.letter_counter -= 1
            return self.letter

    def next(self) -> str:
        return self._get_next_letter() if self.hasNext() else " "

    def hasNext(self) -> bool:
        return self.letter_counter or self.index < len(self.text)


class StringIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    Tags: iterator, generator
    """
    def __init__(self, compressed_string: str):
        self.generator = self._generate(compressed_string)
        self.letter = next(self.generator, " ")  # Preload the first letter

    def _generate(self, compressed_string):
        index = 0
        
        while index < len(compressed_string):
            letter = compressed_string[index]
            index += 1
            frequency = 0
            
            # Parse the number representing the letter frequency
            while (index < len(compressed_string) and 
                   compressed_string[index].isdigit()):
                frequency = 10 * frequency + int(compressed_string[index])
                index += 1
            
            # Yield the letter `frequency` times
            for _ in range(frequency):
                yield letter
        
    def next(self) -> str:
        current_letter = self.letter
        self.letter = next(self.generator, " ")
        return current_letter

    def hasNext(self) -> bool:
        return self.letter != " "


iterator = StringIterator("L1e2t1C1o1d1e1")
print(iterator.next())  # return 'L'
print(iterator.next())  # return 'e'
print(iterator.next())  # return 'e'
print(iterator.next())  # return 't'
print(iterator.next())  # return 'C'
print(iterator.next())  # return 'o'
print(iterator.next())  # return 'd'
print(iterator.hasNext())  # return true
print(iterator.next())  # return 'e'
print(iterator.hasNext())  # return false
print(iterator.next())  # return ' '