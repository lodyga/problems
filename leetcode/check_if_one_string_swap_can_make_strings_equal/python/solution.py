class Solution:
    def areAlmostEqual(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        swap_pair = ()
        is_swapped = False

        for (c1, c2) in zip(text1, text2):
            if (c1 == c2):
                continue

            if (is_swapped):
                return False

            if (swap_pair):
                if swap_pair != (c2, c1):
                    return False

                swap_pair = ()
                is_swapped = True
            else:
                swap_pair = (c1, c2)

        return swap_pair == ()


print(Solution().areAlmostEqual("bank", "kanb") == True)
print(Solution().areAlmostEqual("attack", "defend") == False)
print(Solution().areAlmostEqual("kelb", "kelb") == True)
print(Solution().areAlmostEqual("aa", "ac") == False)
