class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n3)
        Tags: brute-force
        """
        bin_count = [(text.count("0"), text.count("1"))
                     for text in text_list]

        def dfs(index, zeros_counter, ones_counter):
            if index == len(text_list):
                return 0

            # take a number
            take = 0
            if (
                zeros_counter <= m and
                ones_counter <= n
            ):
                take = 1 + dfs(index + 1,
                               zeros_counter + bin_count[index][0],
                               ones_counter + bin_count[index][1]
                               )

            # skip a number
            skip = dfs(index + 1, zeros_counter, ones_counter)

            return max(take, skip)

        return dfs(0, 0, 0)


class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            text_list length
            n size
            m size
        Auxiliary space complexity: O(n3)
        Tags: dp, top-down with memoization as hash map
        Check constraints in recursive case.
        """
        memo = {}
        bin_count = [(text.count("0"), text.count("1"))
                     for text in text_list]

        def dfs(index, zeros_counter, ones_counter):
            if index == len(text_list):
                return 0
            elif (index, zeros_counter, ones_counter) in memo:
                return memo[(index, zeros_counter, ones_counter)]

            # take a number
            take = 0
            if (
                zeros_counter + bin_count[index][0] <= m and
                ones_counter + bin_count[index][1] <= n
            ):
                take = 1 + dfs(index + 1,
                               zeros_counter + bin_count[index][0],
                               ones_counter + bin_count[index][1]
                               )

            # skip a number
            skip = dfs(index + 1, zeros_counter, ones_counter)

            memo[(index, zeros_counter, ones_counter)] = max(take, skip)
            return memo[(index, zeros_counter, ones_counter)]

        return dfs(0, 0, 0)


class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            text_list length
            n size
            m size
        Auxiliary space complexity: O(n3)
        Tags: dp, top-down with memoization as hash map
        Check constraints in base case.
        """
        memo = {}
        bin_count = [(text.count("0"), text.count("1"))
                     for text in text_list]

        def dfs(index, zeros_counter, ones_counter):
            if (  # Invalid solution. (-1) from return counter (1) from take.
                zeros_counter > m or
                ones_counter > n
            ):
                return -1
            elif index == len(text_list):
                return 0
            elif (index, zeros_counter, ones_counter) in memo:
                return memo[(index, zeros_counter, ones_counter)]

            # take a number
            take = 1 + dfs(index + 1,
                           zeros_counter + bin_count[index][0],
                           ones_counter + bin_count[index][1]
                           )

            # skip a number
            skip = dfs(index + 1, zeros_counter, ones_counter)

            memo[(index, zeros_counter, ones_counter)] = max(take, skip)
            return memo[(index, zeros_counter, ones_counter)]

        return dfs(0, 0, 0)


class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            text_list length
            n size
            m size
        Auxiliary space complexity: O(n3)
        Tags: dp, bottom-up
        """
        ROWS = m
        COLS = n
        text_len = len(text_list)

        bin_count = [(text.count("0"), text.count("1"))
                     for text in text_list]

        cache = [[[0] * (COLS + 1)
                 for _ in range(ROWS + 1)]
                 for _ in range(text_len + 1)]

        for index in reversed(range(text_len)):
            zeros, ones = bin_count[index]
            for row in reversed(range(ROWS + 1)):
                for col in reversed(range(COLS + 1)):
                    # skip
                    cache[index][row][col] = cache[index + 1][row][col]
                    # check and take
                    if (
                        # keep indexex in bounds
                        row + zeros <= m and
                        col + ones <= n
                    ):
                        cache[index][row][col] = max(
                            cache[index][row][col],
                            1 + cache[index + 1][row + zeros][col + ones]
                        )

        return cache[0][0][0]


from copy import deepcopy

class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            text_list length
            n size
            m size
        Auxiliary space complexity: O(n2)
        Tags: dp, bottom-up
        Use cache and next cache to store `index + 1` level cache
        """
        ROWS = m
        COLS = n
        text_len = len(text_list)

        bin_count = [(text.count("0"), text.count("1"))
                     for text in text_list]

        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for index in reversed(range(text_len)):
            zeros, ones = bin_count[index]
            next_cache = deepcopy(cache)
            for row in reversed(range(ROWS + 1)):
                for col in reversed(range(COLS + 1)):
                    # skip
                    # Counter is already in place, no neeed for the line below;
                    # cache[row][col] = next_cache[row][col]
                    # check and take
                    if (
                        # keep indexex in bounds
                        row + zeros <= m and
                        col + ones <= n
                    ):
                        cache[row][col] = max(
                            cache[row][col],
                            1 + next_cache[row + zeros][col + ones]
                        )

        return cache[0][0]


class Solution:
    def findMaxForm(self, text_list: list[str], m: int, n: int) -> int:
        """
        Time complexity: O(n3)
            text_list length
            n size
            m size
        Auxiliary space complexity: O(n * m)
        Tags: dp, bottom-up
        Use only one cache
        """
        ROWS = m
        COLS = n
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for zeros, ones in [(s.count('0'), s.count('1')) for s in text_list]:
            # for zeros_used in reversed(range(ROWS - zeros + 1)):
            for zeros_used in range(m, zeros - 1, -1):
                # for ones_used in reversed(range(COLS - ones + 1)):
                for ones_used in range(n, ones - 1, -1):
                    cache[zeros_used][ones_used] = max(
                        cache[zeros_used][ones_used],
                        # 1 + cache[zeros_used + zeros][ones_used + ones]
                        1 + cache[zeros_used - zeros][ones_used - ones]
                    )

        return cache[m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3), 4)
print(Solution().findMaxForm(["10", "0", "1"], 1, 1), 2)
print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 4, 3), 3)