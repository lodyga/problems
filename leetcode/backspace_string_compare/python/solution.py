class Solution:
    def backspaceCompare(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: two pointers
        """
        index1 = len(text1) - 1
        index2 = len(text2) - 1
        back1 = back2 = 0

        while index1 > -1 or index2 > -1:
            while (
                index1 > -1 and
                (text1[index1] == "#" or back1)
            ):
                back1 += 1 if text1[index1] == "#" else -1
                index1 -= 1

            while (
                index2 > -1 and 
                (text2[index2] == "#" or back2)
            ):
                back2 += 1 if text2[index2] == "#" else -1
                index2 -= 1

            if index1 == -1 and index2 == -1:
                return True

            if text1[index1] != text2[index2]:
                return False

            index1 -= 1
            index2 -= 1

        return index1 == index2 == -1


class Solution:
    def backspaceCompare(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: stack
            A: iteration
        """
        text1_clean = self.clean_text(text1)
        text2_clean = self.clean_text(text2)
        return text1_clean == text2_clean

    def clean_text(self, text):
        stack = []

        for letter in text:
            if letter == "#" and stack:
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)


print(Solution().backspaceCompare("ab#c", "ad#c") == True)
print(Solution().backspaceCompare("ab##", "c#d#") == True)
print(Solution().backspaceCompare("a#c", "b") == False)
print(Solution().backspaceCompare("xywrrmp", "xywrrmu#p") == True)
print(Solution().backspaceCompare("nzp#o#g", "b#nzp#o#g") == True)
print(Solution().backspaceCompare("bxj##tw", "bxo#j##tw") == True)
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f") == True)
print(Solution().backspaceCompare("bxj##tw", "bxj###tw") == False)
print(Solution().backspaceCompare("rheyggodcclgstf", "#rheyggodcclgstf") == True)
print(Solution().backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp#######") == False)
print(Solution().backspaceCompare("a", "aa#a") == False)
