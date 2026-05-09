class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        N = len(text)

        def dfs(idx: int) -> int:
            if idx == N:
                return 1

            char = text[idx]

            if char == "0":
                return 0

            res = dfs(idx + 1)

            if (
                idx + 1 < N and
                (char == "1" or
                 char == "2" and text[idx + 1] <= "6")
            ):
                res += dfs(idx + 2)

            return res

        return dfs(0)


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = len(text)
        memo = [-1] * N
        memo.append(1)

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            char = text[idx]

            if char == "0":
                return 0

            res = dfs(idx + 1)

            if (
                idx + 1 < N and
                (char == "1" or
                 char == "2" and text[idx + 1] <= "6")
            ):
                res += dfs(idx + 2)

            memo[idx] = res
            return res

        return dfs(0)


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(text)
        cache = [0] * N
        cache.append(1)

        for idx in range(N - 1, -1, -1):
            char = text[idx]

            if char == "0":
                continue

            cache[idx] = cache[idx + 1]

            if (
                idx + 1 < N and
                (char == "1" or
                 char == "2" and text[idx + 1] <= "6")
            ):
                cache[idx] += cache[idx + 2]

        return cache[0]


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(text)
        cache = [1, 1]

        for idx in range(N - 1, -1, -1):
            char = text[idx]

            if char == "0":
                (cache[0], cache[1]) = (0, cache[0])
                continue

            cache0 = cache[0]

            if (
                idx + 1 < N and
                (char == "1" or
                 char == "2" and text[idx + 1] <= "6")
            ):
                cache0 += cache[1]

            cache[0], cache[1] = cache0, cache[0]

        return cache[0]


print(Solution().numDecodings("5") == 1)
print(Solution().numDecodings("23") == 2)
print(Solution().numDecodings("27") == 1)
print(Solution().numDecodings("226") == 3)
print(Solution().numDecodings("2261") == 3)
print(Solution().numDecodings("12") == 2)
print(Solution().numDecodings("2101") == 1)
print(Solution().numDecodings("06") == 0)
print(Solution().numDecodings("0") == 0)
print(Solution().numDecodings("2617") == 4)
print(Solution().numDecodings("111111111111111111111111111111111111111111111") == 1836311903)
