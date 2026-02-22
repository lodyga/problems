class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: prefix sum, brute-force
        """
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        for right in range(2, len(prefix)):
            num_r = prefix[right]

            for left in range(right - 1):
                num_l = prefix[left]

                if (num_r - num_l) % k == 0:
                    return True

        return False


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list
            A: prefix sum
        """
        prefix = [0]
        diff_index = {0: 0}

        for index, num in enumerate(nums, 1):
            prefix.append((prefix[-1] + num) % k)
            diff = prefix[-1]

            if diff not in diff_index:
                diff_index[diff] = index
            elif index - diff_index[diff] >= 2:
                return True

        return False


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map, list
            A: iteration
        """
        diff = 0
        diff_index = {0: 0}

        for index, num in enumerate(nums, 1):
            diff = (diff + num) % k

            if diff not in diff_index:
                diff_index[diff] = index
            elif index - diff_index[diff] >= 2:
                return True

        return False


print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) == True)
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13) == False)
print(Solution().checkSubarraySum([0], 1) == False)
print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7) == True)
print(Solution().checkSubarraySum([24], 6) == False)
