class Solution:
    def mergeAlternately(self, text1: str, text2: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: two pointers
        """
        left = 0
        right = 0
        text = []

        while (
            left < len(text1) or
            right < len(text2)
        ):
            letter1 = text1[left] if left < len(text1) else ""
            letter2 = text2[right] if right < len(text2) else ""
            text.append(letter1)
            text.append(letter2)
            left += 1
            right += 1

        return "".join(text)


print(Solution().mergeAlternately("abc", "pqr") == "apbqcr")
print(Solution().mergeAlternately("ab", "pqrs") == "apbqrs")
print(Solution().mergeAlternately("abcd", "pq") == "apbqcd")
