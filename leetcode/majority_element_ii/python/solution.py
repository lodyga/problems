class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: iteration
        Boyer-Moore Voting Algorithm
        """
        num_freq = {}

        for num in nums:
            if len(num_freq) == 3:
                for numf in tuple(num_freq):
                    num_freq[numf] -= 1
                    if num_freq[numf] == 0:
                        num_freq.pop(numf)

            num_freq[num] = num_freq.get(num, 0) + 1

        res = []
        for num in num_freq:
            if nums.count(num) / len(nums) > 1 / 3:
                res.append(num)

        return res


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        num_freq = {}
        threshold = len(nums) // 3

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        res = []
        for num, frequency in num_freq.items():
            if frequency > threshold:
                res.append(num)

        return res


print(Solution().majorityElement([3, 3, 4]) == [3])
print(Solution().majorityElement([3, 2, 3]) == [3])
print(Solution().majorityElement([1]) == [1])
print(Solution().majorityElement([1, 2]) == [1, 2])
print(Solution().majorityElement([3, 4, 5, 3, 4]) == [3, 4])
print(Solution().majorityElement([2, 2]) == [2])
print(Solution().majorityElement([3, 4, 5, 3]) == [3])
print(Solution().majorityElement([3, 4, 5]) == [])
print(Solution().majorityElement([1, 2, 3, 4]) == [])
