class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: greedy
        """
        opened = 0
        swaps = 0
        
        for char in s:
            if char == "[":
                opened += 1
            elif opened:  # char == "]"
                opened -= 1
            else:
                opened += 1
                swaps += 1

        return swaps


print(Solution().minSwaps("[]") == 0)
print(Solution().minSwaps("][][") == 1)
print(Solution().minSwaps("]]][[[") == 2)
print(Solution().minSwaps("][[]][][[][]") == 1)
print(Solution().minSwaps("[[[]]]][][]][[]]][[[") == 2)
