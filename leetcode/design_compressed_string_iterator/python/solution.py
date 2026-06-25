class StringIterator:
    """
    Time complexity: 
        O(1): next(), hasNext()
    Auxiliary space complexity: O(n)
    Tags:
        DS: list, string
        A: iterator
    """

    def __init__(self, text) -> None:
        self.text = text
        self.idx = 0
        self.counter = 0
        self._findNext()

    def _findNext(self) -> None:
        if self.counter:
            self.counter -= 1
            return

        while self.idx < len(self.text):
            self.next_letter = self.text[self.idx]
            self.idx += 1
            self.counter = 0

            while (
                self.idx < len(self.text)
                and self.text[self.idx].isdigit()
            ):
                self.counter = self.counter * 10 + int(self.text[self.idx])
                self.idx += 1

            if self.counter == 0:
                continue

            self.counter -= 1
            return

        self.next_letter = " "

    def next(self) -> str:
        res = self.next_letter
        self._findNext()
        return res

    def hasNext(self) -> bool:
        return self.next_letter != " "


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
