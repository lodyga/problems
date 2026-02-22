class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash map
            A: top-down
        """
        memo = {(len(text), True): 0,
                (len(text), False): 0}

        def dfs(index, can_flip_to_1):
            if (index, can_flip_to_1) in memo:
                return memo[(index, can_flip_to_1)]

            letter = text[index]

            if letter == "0":
                # Keep 0 postpone the pivot.
                if can_flip_to_1:
                    res = dfs(index + 1, True)
                # Flip 0 to 1, strat the pivot.
                else:
                    res = 1 + dfs(index + 1, False)

            elif letter == "1":
                # Strat the pivot.
                res = dfs(index + 1, False)

                # Flip 1 to 0 and postpone the pivot.
                if can_flip_to_1:
                    res = min(res, 1 + dfs(index + 1, True))

            memo[(index, can_flip_to_1)] = res
            return res

        return dfs(0, True)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        memo = [[-1] * 2 for _ in range(len(text))]
        memo.append([0, 0])

        def dfs(index, can_flip_to_1):
            if memo[index][can_flip_to_1] != -1:
                return memo[index][can_flip_to_1]

            letter = text[index]

            if letter == "0":
                if can_flip_to_1:
                    res = dfs(index + 1, True)
                else:
                    res = 1 + dfs(index + 1, False)

            elif letter == "1":
                res = dfs(index + 1, False)

                if can_flip_to_1:
                    res = min(res, 1 + dfs(index + 1, True))

            memo[index][can_flip_to_1] = res
            return res

        return dfs(0, True)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [[0, 0] for _ in range(len(text) + 1)]

        # for index, char in reversed(list(enumerate(text))):
        for index in range(len(text) - 1, -1, -1):
            char = text[index]

            if char == "0":
                cache[index][0] = 1 + cache[index + 1][0]
                cache[index][1] = cache[index + 1][1]
            else:
                cache[index][0] = cache[index + 1][0]
                cache[index][1] = min(
                    cache[index + 1][0],
                    1 + cache[index + 1][1]
                )

        return min(cache[0])


class Solution2:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [0, 0]

        for char in reversed(text):
            if char == "0":
                cache[1] = cache[1]
                cache[0] = 1 + cache[0]
            else:  # 0
                cache[1] = min(cache[0], 1 + cache[1])
                cache[0] = cache[0]

        return min(cache)


class Solution:
    def minFlipsMonoIncr(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        ones = 0
        res = 0

        for char in text:
            if char == "1":
                ones += 1
            else:  # 0
                res = min(ones, res + 1)

        return res


print(Solution().minFlipsMonoIncr("00") == 0)
print(Solution().minFlipsMonoIncr("11") == 0)
print(Solution().minFlipsMonoIncr("00110") == 1)
print(Solution().minFlipsMonoIncr("010110") == 2)
print(Solution().minFlipsMonoIncr("00011000") == 2)
print(Solution().minFlipsMonoIncr("0101100011") == 3)
print(Solution().minFlipsMonoIncr("10011111110010111011") == 5)
