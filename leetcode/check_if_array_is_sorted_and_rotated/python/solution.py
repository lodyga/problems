class Solution:
    def check(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        N = len(nums)
        pivot = -1
        
        for index in range(N):
            if nums[index] > nums[(index + 1) % N]:
                pivot += 1
                
                if pivot:
                    return False

        return True


print(Solution().check([3, 4, 5, 1, 2]) == True)
print(Solution().check([2, 1, 3, 4]) == False)
print(Solution().check([1, 2, 3]) == True)
print(Solution().check([6, 10, 6]) == True)
