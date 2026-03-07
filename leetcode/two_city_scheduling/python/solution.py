class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: greedy, sorting
        """
        costs.sort(key=lambda pair: pair[0] - pair[1])
        half = len(costs) // 2

        return (
            sum(a_cost for a_cost, _ in costs[: half]) +
            sum(b_cost for _, b_cost in costs[half:])
        )


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110)
print(Solution().twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859)
print(Solution().twoCitySchedCost([[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086)
