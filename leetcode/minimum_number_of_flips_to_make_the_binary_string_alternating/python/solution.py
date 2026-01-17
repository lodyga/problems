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
        flips_a = 0
        flips_b = 0
        left = 0

        for right in range(N*2 - 1):
            digit = text[right % N]
            flips_a += 1 if digit == str((right + 1) % 2) else 0
            flips_b += 1 if digit == str(right % 2) else 0

            if right + 1 < N:
                continue

            min_flips = min(min_flips, min(flips_a, flips_b))
            # early exit when there are no flips
            if min_flips == 0:
                return 0

            left_digit = text[left]
            flips_a -= 1 if left_digit == str((left + 1) % 2) else 0
            flips_b -= 1 if left_digit == str(left % 2) else 0
            left += 1

        return min_flips


class Solution:
    def minFlips(self, text: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: brute-force
        """
        N = len(text)
        bin_a = "".join(str(num % 2) for num in range(N))
        bin_b = "".join(str((num + 1) % 2) for num in range(N))
        min_flips = N

        for diff in range(N - 1):
            flips_a = 0
            flips_b = 0

            for index in range(N):
                flips_a += 1 if text[(index + diff) % N] != bin_a[index] else 0
                flips_b += 1 if text[(index + diff) % N] != bin_b[index] else 0

            min_flips = min(min_flips, min(flips_a, flips_b))

        return min_flips


print(Solution().minFlips("111000") == 2)
print(Solution().minFlips("010") == 0)
print(Solution().minFlips("1110") == 1)
print(Solution().minFlips("01001001101") == 2)
