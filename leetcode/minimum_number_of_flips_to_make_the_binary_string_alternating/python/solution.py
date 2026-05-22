class Solution:
    def minFlips(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        N = len(text)
        min_flips = N
        s1_flips = 0
        s2_flips = 0

        for right in range(N*2 - 1):
            char = text[right % N]

            if char == str((right + 1) % 2):
                s1_flips += 1

            if char == str(right % 2):
                s2_flips += 1

            if right < N - 1:
                continue

            min_flips = min(min_flips, s1_flips, s2_flips)

            if min_flips == 0:
                return 0

            left = right - N + 1
            
            if text[left] == str((left + 1) % 2):
                s1_flips -= 1
            
            if text[left] == str(left % 2):
                s2_flips -= 1
            
        return min_flips



print(Solution().minFlips("111000") == 2)
print(Solution().minFlips("010") == 0)
print(Solution().minFlips("1110") == 1)
print(Solution().minFlips("01001001101") == 2)