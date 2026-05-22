class Solution:
    def mergeAlternately(self, text1: str, text2: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: two pointers
        """
        res = []
        idx = 0

        while idx < min(len(text1), len(text2)):
            res.append(text1[idx])
            res.append(text2[idx])
            idx += 1
    
        res.append(text1[idx: ])
        res.append(text2[idx: ])

        return "".join(res)


print(Solution().mergeAlternately("abc", "pqr") == "apbqcr")
print(Solution().mergeAlternately("ab", "pqrs") == "apbqrs")
print(Solution().mergeAlternately("abcd", "pq") == "apbqcd")
