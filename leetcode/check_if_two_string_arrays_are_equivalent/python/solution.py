class Solution:
    def arrayStringsAreEqual(self, words1: list[str], words2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        r1 = c1 = r2 = c2 = 0

        while (
            r1 < len(words1) and
            r2 < len(words2)
        ):
            letter1 = words1[r1][c1]
            letter2 = words2[r2][c2]

            if letter1 != letter2:
                return False

            c1 += 1
            if c1 == len(words1[r1]):
                c1 = 0
                r1 += 1

            c2 += 1
            if c2 == len(words2[r2]):
                c2 = 0
                r2 += 1

        return (
            (r1 == len(words1) and c1 == 0) and
            (r2 == len(words2) and c2 == 0)
        )


class Solution:
    def arrayStringsAreEqual(self, words1: list[str], words2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(m+n)
        Tags:
            A: build-in function
        """
        return "".join(words1) == "".join(words2)


class Solution:
    def arrayStringsAreEqual(self, words1: list[str], words2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers generator
        """
        def generate_letter(words):
            for word in words:
                for letter in word:
                    yield letter
            yield False

        letters1 = generate_letter(words1)
        letters2 = generate_letter(words2)

        while True:
            letter1 = next(letters1)
            letter2 = next(letters2)

            if letter1 != letter2:
                return False

            if letter1 is False or letter2 is False:
                return letter1 is letter2 is False


print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True)
print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False)
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True)
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddef"]) == False)
