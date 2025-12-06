class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        N = len(nums)
        concated = [0] * (N * 2)

        for index, num in enumerate(nums):
            concated[index] = num
            concated[index + N] = num

        return concated


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: iteration
        """
        for index in range(len(nums)):
            num = nums[index]
            nums.append(num)
        return nums


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: build-in function
        """
        nums.extend(nums)
        return nums


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: build-in function
        """
        return nums + nums


print(Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1])
print(Solution().getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1])
