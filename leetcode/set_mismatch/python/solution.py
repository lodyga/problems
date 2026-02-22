class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: bit manipulation, negative marking
        """
        nums_copy = nums.copy()
        res = []

        # Find duplicate value.
        for num in nums:
            if nums_copy[abs(num) - 1] < 0:
                res.append(num)
                break

            nums_copy[num - 1] *= -1

        # Find missing value.
        xor = res[0]

        for index, num in enumerate(nums, 1):
            xor ^= index ^ num

        res.append(xor)
        return res


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)

        for num in range(1, len(nums) + 1):
            if num not in num_set:
                missing = num
                break

        return [duplicate, missing]


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
        """
        num_freq = {num: 0 for num in range(1, len(nums) + 1)}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        duplicate = missing = 0
        
        for num, frequency in num_freq.items():
            if frequency == 2:
                duplicate = num
                if missing:
                    break
            elif frequency == 0:
                missing = num
                if duplicate:
                    break

        return [duplicate, missing]


print(Solution().findErrorNums([1, 2, 2, 4]))
print(Solution().findErrorNums([1, 2, 2, 4]) == [2, 3])
print(Solution().findErrorNums([1, 1]) == [1, 2])
print(Solution().findErrorNums([2, 2]) == [2, 1])
print(Solution().findErrorNums([2, 3, 2]) == [2, 1])
