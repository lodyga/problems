class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, Boyer-Moore Voting
        """
        major = 0
        counter = 0

        for num in nums:
            if counter == 0:
                major = num
                counter = 1
            else:
                counter += 1 if major == num else -1

        return major


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        num_frequency = {}
        most_frequent_number = nums[0] + 1
        most_frequency = 0

        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1
            if num_frequency[num] > most_frequency:
                most_frequent_number = num
                most_frequency = num_frequency[num]

        return most_frequent_number


print(Solution().majorityElement([3, 2, 3]) == 3)
print(Solution().majorityElement([3, 3, 4]) == 3)
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
