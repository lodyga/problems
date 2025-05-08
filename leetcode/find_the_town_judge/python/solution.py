class Solution:
    def findJudge(self, people_count: int, trust_list: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set, hash map
        """
        if people_count == 1 and not trust_list:
            return 1

        trustees = set()
        trusters = {}

        for trustee, truster in trust_list:
            trustees.add(trustee)
            trusters[truster] = trusters.get(truster, 0) + 1

        for truster, trustier_approval in trusters.items():
            if (truster not in trustees and 
                    trustier_approval == people_count - 1):
                return truster

        return -1


print(Solution().findJudge(2, [[1, 2]]), 2)
print(Solution().findJudge(3, [[1, 3], [2, 3]]), 3)
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)
print(Solution().findJudge(3, [[1, 2], [2, 3]]), -1)
print(Solution().findJudge(1, []), 1)
print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3)