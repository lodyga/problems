class Solution:
    def backspaceCompare(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        def clean_text(text):
            stack = []

            for char in text:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)

            return "".join(stack)
        
        cleaned_text1 = clean_text(text1)
        cleaned_text2 = clean_text(text2)

        return cleaned_text1 == cleaned_text2


class Solution:
    def backspaceCompare(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        def get_letter_idx(start, text):
            backspace = 0

            while start > - 1 and (text[start] == "#" or backspace):
                backspace += 1 if text[start] == "#" else - 1
                start -= 1

            return start

        idx1 = len(text1) - 1
        idx2 = len(text2) - 1

        while True:
            idx1 = get_letter_idx(idx1, text1)
            idx2 = get_letter_idx(idx2, text2)

            if idx1 < 0 and idx2 < 0:
                return True
            elif idx1 < 0 or idx2 < 0:
                return False

            char1 = text1[idx1]
            char2 = text2[idx2]

            if char1 != char2:
                return False

            idx1 -= 1
            idx2 -= 1


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
