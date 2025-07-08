r"""
draft
[3, 4] scores
[8, 7] ages

                    .
            /               \
            3               0
        /       \       /       \
        -       0       4       0

[4, 5, 6, 5] scores
[2, 1, 2, 1] ages

                           .
                /4                       \4
                4                        0
       /5-            \5              /5          \5
                      5             5              0
                   /6  \6        /6    \6-       /6    \6
                 11     5      11           
              /5  \5            
             16   11


"""


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        stats = list(zip(scores, ages))
        stats.sort()
        cache = [score for score, _ in stats]

        for right in range(1, len(stats)):
            score, age = stats[right]
            
            for left in range(right):
                _, prev_age = stats[left]
                if prev_age <= age:
                    cache[right] = max(cache[right], score + cache[left])

        return max(cache)


print(Solution().bestTeamScore([3, 4], [7, 8]) == 7)
print(Solution().bestTeamScore([4, 3], [7, 8]) == 4)
print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34)
print(Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 5, 4, 3]) == 19)
print(Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16)
print(Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6)
print(Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]) == 29)
print(Solution().bestTeamScore([6, 5, 1, 7, 6, 5, 5, 4, 10, 4], [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]) == 43)


# wrong approach
class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization
        """
        stats = list(zip(ages, scores))
        stats.sort(key=lambda x: (x[0], x[1]))
        memo = {}

        def dfs(index, prev_index):
            if index == len(stats):
                return 0
            elif (index, prev_index) in memo:
                return memo[(index, prev_index)]

            age, score = stats[index]

            if (  # if conflict occured
                age < stats[index + 1][0] and
                score > stats[index + 1][1]
            ):
                # skip current player
                lis = dfs(index + 1, prev_index)
            else:  # no conflict
                lis = score + dfs(index + 1, index)


            memo[(index, prev_index)] = lis
            return lis

        dfs(0, -1)
        return memo[0]
