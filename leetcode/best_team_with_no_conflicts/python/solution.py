class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        data = sorted(zip(scores, ages))
        # [starting index + 1: LIS length]
        memo = [-1] * (len(data) + 1)

        def dfs(index, prev_index):
            if index == len(data):
                return 0
            elif memo[prev_index + 1] != -1:
                return memo[prev_index + 1]

            prev_age = -1
            if prev_index != -1:
                _, prev_age = data[prev_index]
            score, age = data[index]

            # skip current score
            skip = dfs(index + 1, prev_index)
            # take current score
            take = 0
            if age >= prev_age:
                take = score + dfs(index + 1, index)

            lis = max(skip, take)
            memo[prev_index + 1] = lis
            return lis

        return dfs(0, -1)


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        data = sorted(zip(scores, ages))
        # [starting index + 1: LIS length]
        cache = [score for score, _ in data]

        for left in range(len(data) - 1, -1, -1):
            score, age = data[left]
            
            for right in range(left + 1, len(data)):
                _, next_age = data[right]
            
                if age <= next_age:
                    cache[left] = max(cache[left], score + cache[right])

        return max(cache)


print(Solution().bestTeamScore([3, 4], [7, 8]) == 7)
print(Solution().bestTeamScore([4, 3], [7, 8]) == 4)
print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34)
print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 5, 4, 3]) == 19)
print(Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16)
print(Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6)
print(Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]) == 29)
print(Solution().bestTeamScore([6, 5, 1, 7, 6, 5, 5, 4, 10, 4], [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]) == 43)
