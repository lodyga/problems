class Solution:
    def nextPermutation(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, two pointers, in-place
        """
        N = len(nums)
        
        # Step 1: find pivot
        pivot = N - 2
        while (
            pivot > -1 and 
            nums[pivot] >= nums[pivot + 1]
        ):
            pivot -= 1

        # Step 2: find rightmost successor
        if pivot > -1:
            index = N - 1
            while nums[pivot] >= nums[index]:
                index -= 1
            nums[pivot], nums[index] = nums[index], nums[pivot]

        # Step 3: reverse the suffix
        left = pivot + 1
        right = N - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


print(Solution().nextPermutation([1, 2, 3, 6, 5, 4]) == [1, 2, 4, 3, 5, 6])
print(Solution().nextPermutation([1, 2, 3]) == [1, 3, 2])
print(Solution().nextPermutation([3, 2, 1]) == [1, 2, 3])
print(Solution().nextPermutation([1, 1, 5]) == [1, 5, 1])
print(Solution().nextPermutation([1, 2, 3, 4]) == [1, 2, 4, 3])
print(Solution().nextPermutation([1, 2, 4, 3]) == [1, 3, 2, 4])
print(Solution().nextPermutation([1, 3, 2, 4]) == [1, 3, 4, 2])
print(Solution().nextPermutation([1, 3, 4, 2]) == [1, 4, 2, 3])
print(Solution().nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4])
print(Solution().nextPermutation([4, 3, 2, 1]) == [1, 2, 3, 4])
