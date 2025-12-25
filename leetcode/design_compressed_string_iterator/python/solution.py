class StringIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list, string
        A: iterator
    """

    def __init__(self, text) -> None:
        self.text = text
        self.index = 0
        self.letter = ""
        self.letter_counter = 0

    def _get_next_letter(self) -> str:
        self.letter = self.text[self.index]
        self.index += 1

        multi = 0
        while (
            self.index < len(self.text) and
            self.text[self.index].isdigit()
        ):
            multi = multi*10 + int(self.text[self.index])
            self.index += 1
        self.letter_counter = multi - 1

        return self.letter

    def next(self) -> str:
        if self.letter_counter:
            next_letter = self.letter
            self.letter_counter -= 1
            if self.letter_counter == 0:
                self.letter = ""
            return next_letter
        elif self.index == len(self.text):
            return " "
        else:
            return self._get_next_letter()

    def hasNext(self) -> bool:
        return bool(
            self.letter_counter or
            self.index < len(self.text)
        )


iterator = StringIterator("L1e2t1C1o1d1e1")
print(iterator.next() == "L")
print(iterator.next() == "e")
print(iterator.next() == "e")
print(iterator.next() == "t")
print(iterator.next() == "C")
print(iterator.next() == "o")
print(iterator.next() == "d")
print(iterator.hasNext() is True)
print(iterator.next() == "e")
print(iterator.hasNext() is False)
print(iterator.next() == " ")
