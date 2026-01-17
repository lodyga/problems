class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        N = len(gas)
        # return [gas[index] - cost[index] for index in range(N)]

        for start in range(N):
            gas_tank = 0
            can_complete = True

            for index in range(start, start + N):
                gas_tank += gas[index % N] - cost[index % N]
                if gas_tank < 0:
                    can_complete = False
                    break

            if can_complete:
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
        if sum(gas) < sum(cost):
            return -1
        
        gas_tank = 0
        start = 0

        for index in range(len(gas)):
            gas_tank += gas[index] - cost[index]

            if gas_tank < 0:
                gas_tank = 0
                start = index + 1
            
        return start


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3)
print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1)
print(Solution().canCompleteCircuit([1, 2, 3, 4],  [2, 2, 4, 1]) == 3)
print(Solution().canCompleteCircuit([3, 1, 1],  [1, 2, 2]) == 0)
