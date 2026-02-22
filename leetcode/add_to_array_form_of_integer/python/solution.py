class Solution:
    def addToArrayForm(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        nums.reverse()
        index = 0

        while k:
            if index == len(nums):
                nums.append(0)
            
            nums[index] += k % 10
            k //= 10

            if nums[index] > 9:
                nums[index] -= 10
                k += 1

            index += 1

        nums.reverse()
        return nums


print(Solution().addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4])
print(Solution().addToArrayForm([2, 7, 4], 181) == [4, 5, 5])
print(Solution().addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1])
print(Solution().addToArrayForm([9, 9], 1) == [1, 0, 0])
