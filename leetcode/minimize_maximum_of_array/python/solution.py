class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, prefix sum
        """
        prefix = 0
        res = nums[0]
        
        for index, num in enumerate(nums):
            prefix += num
            avg = ((prefix - 1) // (index + 1)) + 1
            res = max(res, avg)
            
        return res


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: greedy, prefix sum
        """
        N = len(nums)
        prefix = [0]
        avg = []
        counter = 1

        for num in nums:
            prefix.append(prefix[-1] + num)
            avg.append(((prefix[-1] - 1) // counter) + 1)
            counter += 1

        for index in range(N - 1, 0, -1):
            num = nums[index]
            avg[index - 1] = max(avg[index - 1], avg[index])

            if num > avg[index]:
                diff = num - avg[index]
                nums[index] -= diff
                nums[index - 1] += diff

        return max(nums)


print(Solution().minimizeArrayValue([3, 7, 1, 6]) == 5)
print(Solution().minimizeArrayValue([10, 1]) == 10)
print(Solution().minimizeArrayValue([13, 13, 20, 0, 8, 9, 9]) == 16)
