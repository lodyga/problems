class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        for left in range(len(gas)):
            gas_tank = 0

            for right in range(left, len(gas) + left):
                gas_tank += gas[right % len(gas)] - cost[right % len(gas)]
                if gas_tank < 0:
                    break
                elif right == len(gas) + left - 1:
                    return left

        return -1


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        gas_tank = 0  # sliding window
        left = 0
        right = 0

        while right < 2 * len(gas) - 1:
            gas_tank += gas[right % len(gas)] - cost[right % len(gas)]

            while left <= right and gas_tank < 0:
                gas_tank -= gas[left % len(gas)] - cost[left % len(gas)]
                left += 1
            
            if right - left + 1 == len(gas):
                return left
            right += 1

        return -1


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
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


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)
print(Solution().canCompleteCircuit([1, 2, 3, 4],  [2, 2, 4, 1]), 3)
print(Solution().canCompleteCircuit([3, 1, 1],  [1, 2, 2]), 0)