class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)

        for start in range(N):
            tank = 0

            for idx in range(start, start + N):
                tank += gas[idx % N] - cost[idx % N]

                if tank < 0:
                    break

            if tank >= 0:
                return start

        return -1


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        N = len(gas)
        tank = 0
        start = 0

        for idx in range(2 * N - 1):
            tank += gas[idx % N] - cost[idx % N]

            if tank < 0:
                tank = 0
                start = idx + 1
                continue
            elif idx - start == N - 1:
                return idx + 1 - N

        return -1


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)
        tank = 0
        start = 0

        for idx in range(N):
            tank += gas[idx] - cost[idx]

            if tank < 0:
                tank = 0
                start = idx + 1

        return start


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3)
print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1)
print(Solution().canCompleteCircuit([1, 2, 3, 4],  [2, 2, 4, 1]) == 3)
print(Solution().canCompleteCircuit([3, 1, 1],  [1, 2, 2]) == 0)
