class Solution:
    def findJudge(self, n: int, trust_list: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        if n == 1 and not trust_list:
            return 1
        
        trust_freq = {}
        trusters = set()

        for a, b in trust_list:
            trust_freq[b] = trust_freq.get(b, 0) + 1
            trusters.add(a)

        for key, val in trust_freq.items():
            if val == n - 1 and key not in trusters:
                return key

        return -1


class Solution:
    def findJudge(self, n: int, trust_list: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: iteration
        """
        # [person: votes]
        votes = [0] * n

        for a, b in trust_list:
            votes[a - 1] = -1
            if votes[b - 1] != -1:
                votes[b - 1] += 1
        
        for index, vote in enumerate(votes):
            if vote == n - 1:
                return index + 1

        return -1


print(Solution().findJudge(2, [[1, 2]]) == 2)
print(Solution().findJudge(3, [[1, 3], [2, 3]]) == 3)
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1)
print(Solution().findJudge(3, [[1, 2], [2, 3]]) == -1)
print(Solution().findJudge(1, []) == 1)
print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3)
