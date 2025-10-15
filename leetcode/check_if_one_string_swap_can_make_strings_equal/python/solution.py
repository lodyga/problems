class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        is_changed = None
        for index in range(len(s1)):
            if s1[index] == s2[index]:
                continue
            elif is_changed == None:
                is_changed = True
                changeIndex = index
            elif is_changed == True:
                is_changed = False
                if (
                    s1[changeIndex] != s2[index] or
                    s1[index] != s2[changeIndex]
                ):
                    return False
            elif is_changed == False:
                return False

        return is_changed in (None, False)


print(Solution().areAlmostEqual("bank", "kanb") == True)
print(Solution().areAlmostEqual("attack", "defend") == False)
print(Solution().areAlmostEqual("kelb", "kelb") == True)
print(Solution().areAlmostEqual("aa", "ac") == False)