class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers
        """
        people.sort()
        left = 0
        right = len(people) - 1
        boat_counter = 0

        while left <= right:
            if people[left] <= limit - people[right]:
                left += 1
            right -= 1
            boat_counter += 1

        return boat_counter


print(Solution().numRescueBoats([1, 2], 3) == 1)
print(Solution().numRescueBoats([3, 2, 2, 1], 3) == 3)
print(Solution().numRescueBoats([3, 5, 3, 4], 5) == 4)
print(Solution().numRescueBoats([3, 2, 3, 2, 2], 6) == 3)
print(Solution().numRescueBoats([2, 4], 5) == 2)
