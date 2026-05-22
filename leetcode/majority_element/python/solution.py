class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, voting
        """
        major_val = 0
        major_freq = 0

        for num in nums:
            if major_freq == 0:
                major_val = num
                major_freq = 1
            elif num == major_val:
                major_freq += 1
            else:
                major_freq -= 1
        
        return major_val


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, voting
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
        num_freq = {}
        
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            elif num_freq:
                major_num = next(iter(num_freq))
                num_freq[major_num] -= 1
            
                if num_freq[major_num] == 0:
                    num_freq.pop(major_num)
            else:
                num_freq[num] = 1

        return next(iter(num_freq))


print(Solution().majorityElement([3, 2, 3]) == 3)
print(Solution().majorityElement([3, 3, 4]) == 3)
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
