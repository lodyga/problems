class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing stack
            A: iteration
        """
        stack = []
        prev_min = nums[0]

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and stack[-1][1] < num:
            # if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            
            stack.append((num, prev_min))
            prev_min = min(prev_min, num)

        return False


print(Solution().find132pattern([3, 1, 4, 2]) == True)
print(Solution().find132pattern([1, 2, 3, 4]) == False)
print(Solution().find132pattern([-1, 3, 2, 0]) == True)
print(Solution().find132pattern([3, 5, 0, 3, 4]) == True)
print(Solution().find132pattern([1, 0, 1, -4, -3]) == False)
print(Solution().find132pattern([-2, 1, 2, -2, 1, 2]) == True)
print(Solution().find132pattern([1, 2, 3, 4, -4, -3, -5, -1]) == False)
print(Solution().find132pattern([1, 3, -4, 2]) == True)


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        for right, num in enumerate(nums[2:], 2):
            mid = right - 1

            while mid > 0:
                if nums[mid] > num:
                    left = mid - 1

                    while left >= 0:
                        if nums[left] < num:
                            return True

                        left -= 1

                mid -= 1

        return False


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False
