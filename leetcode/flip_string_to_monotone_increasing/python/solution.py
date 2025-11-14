class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute_force
        """
        def dfs(index, can_change_to_1):
            if index == len(text):
                return 0

            flips = len(text)

            if text[index] == "0":
                # pass current number
                if can_change_to_1:
                    flips = min(flips, dfs(index + 1, True))
                # flip current number
                flips = min(flips, 1 + dfs(index + 1, False))

            elif text[index] == "1":
                # pass current number
                flips = min(flips, dfs(index + 1, False))
                if can_change_to_1:
                    # flip current number
                    flips = min(flips, 1 + dfs(index + 1, True))

            return flips

        return dfs(0, True)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {(len(text), True): 0, (len(text), False): 0}

        def dfs(index, can_change_to_1):
            if (index, can_change_to_1) in memo:
                return memo[(index, can_change_to_1)]

            flips = len(text)

            if text[index] == "0":
                # pass current number
                if can_change_to_1:
                    flips = min(flips, dfs(index + 1, True))
                # flip current number
                flips = min(flips, 1 + dfs(index + 1, False))

            elif text[index] == "1":
                # pass current number
                flips = min(flips, dfs(index + 1, False))
                if can_change_to_1:
                    # flip current number
                    flips = min(flips, 1 + dfs(index + 1, True))

            memo[(index, can_change_to_1)] = flips
            return flips

        return dfs(0, True)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = [[-1, -1] for _ in range(len(text) + 1)]
        memo[-1] = [0, 0]

        def dfs(index, can_change_to_1):
            if memo[index][can_change_to_1] != -1:
                return memo[index][can_change_to_1]

            flips = len(text)

            if text[index] == "0":
                # pass current number
                if can_change_to_1:
                    flips = min(flips, dfs(index + 1, True))
                # flip current number
                flips = min(flips, 1 + dfs(index + 1, False))

            elif text[index] == "1":
                # pass current number
                flips = min(flips, dfs(index + 1, False))
                if can_change_to_1:
                    # flip current number
                    flips = min(flips, 1 + dfs(index + 1, True))

            memo[index][can_change_to_1] = flips
            return flips

        return dfs(0, True)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [[0, 0] for _ in range(len(text) + 1)]

        for index, char in reversed(list(enumerate(text))):
            if char == "0":
                cache[index][0] = 1 + cache[index + 1][0]
                cache[index][1] = min(
                    1 + cache[index + 1][0], cache[index + 1][1])
            else:
                cache[index][0] = cache[index + 1][0]
                cache[index][1] = min(
                    cache[index + 1][0], 1 + cache[index + 1][1])

        return min(cache[0])


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = [0, 0]

        for char in reversed(text):
            if char == "0":
                cache[1] = min(1 + cache[0], cache[1])
                cache[0] = 1 + cache[0]
            else:
                cache[1] = min(cache[0], 1 + cache[1])
                cache[0] = cache[0]

        return min(cache)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        ones = 0
        flips = 0
        for char in text:
            if char == "1":
                ones += 1
            else:
                flips = min(ones, flips + 1)

        return flips


print(Solution().minFlipsMonoIncr("00") == 0)
print(Solution().minFlipsMonoIncr("11") == 0)
print(Solution().minFlipsMonoIncr("00110") == 1)
print(Solution().minFlipsMonoIncr("010110") == 2)
print(Solution().minFlipsMonoIncr("00011000") == 2)
print(Solution().minFlipsMonoIncr("0101100011") == 3)
print(Solution().minFlipsMonoIncr("10011111110010111011") == 5)
