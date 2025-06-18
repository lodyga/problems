class Solution:
    def findDuplicate(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        Floyd's cycle finding algorithm or Hare-Tortoise algorithm        
        """
        slow = 0
        fast = 0
        
        # find the intersection
        while True:
            slow = numbers[slow]
            fast = numbers[numbers[fast]]
            if slow == fast:
                break
            
        
        # find the beginning of the cycle
        # The distance from the intersection to the beginning of the cycle is the same as
        # from the beginning of the graph to the beginning of the cycle.
        slow2 = 0
        while True:
            slow = numbers[slow]
            slow2 = numbers[slow2]
            if slow == slow2:
                return slow


print(Solution().findDuplicate([1, 3, 4, 2, 2]), 2)
print(Solution().findDuplicate([3, 1, 3, 4, 2]), 3)
print(Solution().findDuplicate([3, 3, 3, 3, 3]), 3)
print(Solution().findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]), 9)
print(Solution().findDuplicate([2, 1, 2]), 2)