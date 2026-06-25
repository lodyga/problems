class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: iteration
        """
        # [person: votes]
        votes = [0] * n

        for trusting, trusted in trust:
            votes[trusting - 1] = -1
            votes[trusted - 1] += 1
        
        for idx, vote in enumerate(votes):
            if vote == n - 1:
                return idx + 1

        return -1


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: iteration
        """
        # [person: total votes]
        votes = [0] * n
        has_voted = [False] * n

        for trusting, trusted in trust:
            votes[trusted - 1] += 1
            has_voted[trusting - 1] = True
        
        for idx, vote in enumerate(votes):
            if (
                vote == n - 1 
                and has_voted[idx] is False
            ):
                return idx + 1

        return -1


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        if n == 1 and not trust:
            return 1
        
        trust_freq = {}
        trusters = set()

        for trusting, trusted in trust:
            trust_freq[trusted] = trust_freq.get(trusted, 0) + 1
            trusters.add(trusting)

        for key, val in trust_freq.items():
            if val == n - 1 and key not in trusters:
                return key

        return -1


print(Solution().findJudge(2, [[1, 2]]) == 2)
print(Solution().findJudge(3, [[1, 3], [2, 3]]) == 3)
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1)
print(Solution().findJudge(3, [[1, 2], [2, 3]]) == -1)
print(Solution().findJudge(1, []) == 1)
print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3)
