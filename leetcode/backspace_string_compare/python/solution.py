class Solution:
    def backspaceCompare(self, word1: str, word2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        index1 = len(word1) - 1
        index2 = len(word2) - 1

        def backspace_trailing(text, index):
            """
            Backspace trailing characters.
            """
            skip = 0

            while (index >= 0 and
                   (text[index] == "#" or
                    skip)):
                skip += 1 if text[index] == "#" else -1
                index -= 1

            return index

        while index1 >= 0 and index2 >= 0:
            index1 = backspace_trailing(word1, index1)
            index2 = backspace_trailing(word2, index2)

            if index1 >= 0 and index2 >= 0 and word1[index1] != word2[index2]:
                return False

            index1 -= 1
            index2 -= 1

        # when the rest of one of the non-empty string can be folded to none
        if index1 >= 0:
            index1 = backspace_trailing(word1, index1)
        if index2 >= 0:
            index2 = backspace_trailing(word2, index2)

        return index1 == index2


class Solution:
    def backspaceCompare(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        text1_clean = self.clean_text(text1)
        text2_clean = self.clean_text(text2)

        return text1_clean == text2_clean

    def clean_text(self, text):
        stack = []

        for letter in text:
            if letter == "#":
                stack and stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)


print(Solution().backspaceCompare("ab#c", "ad#c"), True)
print(Solution().backspaceCompare("ab##", "c#d#"), True)
print(Solution().backspaceCompare("a#c", "b"), False)
print(Solution().backspaceCompare("xywrrmp", "xywrrmu#p"), True)
print(Solution().backspaceCompare("nzp#o#g", "b#nzp#o#g"), True)
print(Solution().backspaceCompare("bxj##tw", "bxo#j##tw"), True)
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"), True)
print(Solution().backspaceCompare("bxj##tw", "bxj###tw"), False)
print(Solution().backspaceCompare("rheyggodcclgstf", "#rheyggodcclgstf"), True)
print(Solution().backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp#######"), False)