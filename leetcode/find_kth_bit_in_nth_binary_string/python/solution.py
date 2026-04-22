class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(2^n)
        Tags:
            DS: list
            A: iteration
        """
        bits = ["0"]

        while True:
            if len(bits) >= k:
                return bits[k - 1]

            bits.append("1")

            for idx in range(len(bits) - 2, -1, -1):
                bit = "1" if bits[idx] == "0" else "0"
                bits.append(bit)


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: recursion
        """
        length = 2**n - 1

        def dfs(lenght, k):
            if lenght == 1:
                return "0"

            half = lenght // 2

            if k <= half:
                return dfs(half, k)
            elif k > half + 1:
                return "1" if dfs(half, 1 + lenght - k) == "0" else "0"
            else:
                return "1"

        return dfs(length, k)


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: recursion
        """
        length = 2**n - 1

        def dfs(lenght, k, invert):
            if lenght == 1:
                return "0" if not invert else "1"

            half = lenght // 2

            if k <= half:
                return dfs(half, k, invert)
            elif k > half + 1:
                return dfs(half, 1 + lenght - k, not invert)
            else:
                return "1" if not invert else "0"

        return dfs(length, k, False)


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        length = 2**n - 1
        invert = False

        while length > 1:
            half = length // 2

            if k <= half:
                length = half
            elif k > half + 1:
                k = 1 + length - k
                length = half
                invert = not invert
            else:
                return "1" if not invert else "0"

        return "0" if not invert else "1"


print(Solution().findKthBit(3, 1) == "0")
print(Solution().findKthBit(4, 11) == "1")
print(Solution().findKthBit(2, 3) == "1")
