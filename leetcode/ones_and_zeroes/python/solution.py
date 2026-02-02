class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            O(strs_len * m * n)
            strs_len: strs length
            m: m value
            n: n value
        Auxiliary space complexity: O(n3)
        Tags:
            DS: hash map
            A: top-down
        """
        N = len(strs)
        bins = [(text.count("0"), text.count("1")) for text in strs]
        memo = {}

        def dfs(index: int, zeros: int, ones: int) -> int:
            memo_ind = (index, zeros, ones)
            if zeros < 0 or ones < 0:
                return -1
            elif index == N:
                return 0
            elif memo_ind in memo:
                return memo[memo_ind]

            z, o = bins[index]

            skip = dfs(index + 1, zeros, ones)
            take = 1 + dfs(index + 1, zeros - z, ones - o)

            res = max(skip, take)
            memo[memo_ind] = res
            return res

        return dfs(0, m, n)


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            O(strs_len * m * n)
            strs_len: strs length
            m: m value
            n: n value
        Auxiliary space complexity: O(n3)
        Tags:
            DS: array
            A: top-down
        """
        N = len(strs)
        bins = [(text.count("0"), text.count("1")) for text in strs]
        memo = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(N)]

        def dfs(index: int, zeros: int, ones: int) -> int:
            if zeros < 0 or ones < 0:
                return -1
            elif index == N:
                return 0
            elif memo[index][zeros][ones] != -1:
                return memo[index][zeros][ones]

            z, o = bins[index]

            skip = dfs(index + 1, zeros, ones)
            take = 1 + dfs(index + 1, zeros - z, ones - o)

            res = max(skip, take)
            memo[index][zeros][ones] = res
            return res

        return dfs(0, m, n)


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            O(strs_len * m * n)
            strs_len: strs length
            m: m value
            n: n value
        Auxiliary space complexity: O(n3)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(strs)
        bins = [(text.count("0"), text.count("1")) for text in strs]
        cache = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(N + 1)]

        for index in range(N - 1, -1, -1):
            for zeros in range(m, -1, -1):
                for ones in range(n, -1, -1):
                    z, o = bins[index]
                    cache[index][zeros][ones] = cache[index + 1][zeros][ones]

                    if zeros + z <= m and ones + o <= n:
                        cache[index][zeros][ones] = max(
                            cache[index][zeros][ones],
                            (1 + cache[index + 1][zeros + z][ones + o])
                        )

        return cache[0][0][0]


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            O(strs_len * m * n)
            strs_len: strs length
            m: m value
            n: n value
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(strs)
        bins = [(text.count("0"), text.count("1")) for text in strs]
        next_cache = [[0] * (n + 1) for _ in range(m + 1)]

        for index in range(N - 1, -1, -1):
            cache = [[0] * (n + 1) for _ in range(m + 1)]
            z, o = bins[index]

            for zeros in range(m, -1, -1):
                for ones in range(n, -1, -1):
                    cache[zeros][ones] = next_cache[zeros][ones]

                    if zeros + z <= m and ones + o <= n:
                        cache[zeros][ones] = max(
                            cache[zeros][ones],
                            (1 + next_cache[zeros + z][ones + o])
                        )

            next_cache = cache

        return next_cache[0][0]


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            O(strs_len * m * n)
            strs_len: strs length
            m: m value
            n: n value
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [[0] * (n + 1) for _ in range(m + 1)]

        for st in strs:
            (z, o) = (st.count("0"), st.count("1"))

            for zeros in range(m, z - 1, -1):
                for ones in range(n, o - 1, -1):
                    cache[zeros][ones] = max(
                        cache[zeros][ones],
                        1 + cache[zeros - z][ones - o]
                    )

        return cache[m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4)
print(Solution().findMaxForm(["10", "0", "1"], 1, 1) == 2)
print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 4, 3) == 3)
