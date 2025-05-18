class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        cars = sorted(zip(positions, speeds), reverse=True)
        times_to_finish = [(target - position) / speed for position, speed in cars]
        
        fleet_count = 1
        for index, time in enumerate(times_to_finish[1:], 1):
            if times_to_finish[index - 1] < time:
                fleet_count += 1
            else:
                # when the car joins fleet match its speed
                times_to_finish[index] = times_to_finish[index - 1]
        return fleet_count


# O(nlogn), O(n)
class Solution:
    def carFleet(self, target, positions, speeds):
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        cars = sorted(zip(positions, speeds), reverse=True)
        fleet_stack = []

        for position, speed in cars:
            time_to_target = (target - position) / speed
            
            if fleet_stack and fleet_stack[-1] >= time_to_target:
                # when the car joins fleet match its speed
                continue

            fleet_stack.append(time_to_target)  # append fleet leader car time to fleet stack

        return len(fleet_stack)


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
print(Solution().carFleet(10, [3], [3]), 1)
print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]), 1)
print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]), 1)