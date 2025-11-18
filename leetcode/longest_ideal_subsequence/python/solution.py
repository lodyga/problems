class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        index
        """
        def dfs(index, prev_index):
            if index == len(text):
                return 0

            # sikp current number
            longest = dfs(index + 1, prev_index)

            # take current number
            if (
                prev_index == -1 or
                0 <= abs(ord(text[index]) - ord(text[prev_index])) <= k
            ):
                longest = max(longest, 1 + dfs(index + 1, index))

            return longest

        return dfs(0, -1)


class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        letter
        """
        def dfs(index, prev_letter):
            if index == len(text):
                return 0

            # sikp current number
            longest = dfs(index + 1, prev_letter)

            # take current number
            if (
                prev_letter == "" or
                0 <= abs(ord(text[index]) - ord(prev_letter)) <= k
            ):
                longest = max(longest, 1 + dfs(index + 1, text[index]))

            return longest

        return dfs(0, "")


class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map, tle
        index
        """
        # {subsequence starting index: longest subsequence length}
        memo = {}

        def dfs(index, prev_index):
            if index == len(text):
                return 0
            elif prev_index in memo:
                return memo[prev_index]

            # sikp current number
            longest = dfs(index + 1, prev_index)

            # take current number
            if (
                prev_index == -1 or
                0 <= abs(ord(text[index]) - ord(text[prev_index])) <= k
            ):
                longest = max(longest, 1 + dfs(index + 1, index))

            memo[prev_index] = longest
            return longest

        return dfs(0, -1)


class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        index
        """
        # index: current letter index
        # prev letter index: subsequence first letter index
        # {(index, prev_letter_index): longest subsequence length}
        memo = {}

        def dfs(index, prev_letter_index):
            if index == len(text):
                return 0
            if (index, prev_letter_index) in memo:
                return memo[(index, prev_letter_index)]

            # sikp current number
            longest = dfs(index + 1, prev_letter_index)
            letter_index = ord(text[index]) - ord('a')
            
            # take current number
            if (
                prev_letter_index == -1 or 
                abs(letter_index - prev_letter_index) <= k
            ):
                longest = max(longest, 1 + dfs(index + 1, letter_index))
            
            memo[(index, prev_letter_index)] = longest
            return longest

        return dfs(0, -1)


class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array, tle
        """
        # [subsequence starting index: longest subsequence length]
        memo = [-1] * len(text)

        def dfs(index, prev_index):
            if index == len(text):
                return 0
            elif memo[prev_index] != -1:
                return memo[prev_index]

            # sikp current number
            longest = dfs(index + 1, prev_index)

            # take current number
            if (
                prev_index == -1 or
                0 <= abs(ord(text[index]) - ord(text[prev_index])) <= k
            ):
                longest = max(longest, 1 + dfs(index + 1, index))

            memo[prev_index] = longest
            return longest

        return dfs(0, -1)


class Solution:
    def longestIdealString(self, text: str, k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up, tle
        """
        # [subsequence starting index: longest subsequence length]
        cache = [1] * len(text)

        for index in reversed(range(len(text) - 1)):
            for i2 in range(index + 1, len(text)):
                if 0 <= abs(ord(text[index]) - ord(text[i2])) <= k:
                    cache[index] = max(
                        cache[index],
                        1 + cache[i2]
                    )
        return max(cache)


print(Solution().longestIdealString("abcd", 3), 4)
print(Solution().longestIdealString("acfgbd", 2), 4)
print(Solution().longestIdealString("pvjcci", 3), 2)
print(Solution().longestIdealString("dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7) , 42)
print(Solution().longestIdealString("acfgbd", 2) == 4)
print(Solution().longestIdealString("abcd", 3) == 4)
print(Solution().longestIdealString("pvjcci", 3) == 2)
print(Solution().longestIdealString("dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7) == 42)
