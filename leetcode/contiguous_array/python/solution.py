class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: prefix sum
        """
        # Ones over zeros surplus counter.
        ones_surp = 0
        res = 0
        # Ones over zeros surplus: index of first occurence.
        prefix_index = {}

        for index, num in enumerate(nums):
            ones_surp += 1 if num else -1

            if ones_surp not in prefix_index:
                prefix_index[ones_surp] = index

            if ones_surp == 0:
                res = max(res, index + 1)
            elif ones_surp in prefix_index:
                res = max(res, index - prefix_index[ones_surp])

        return res


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, tuple
            A: prefix sum
        """
        prefix = [(0, 0)]

        for num in nums:
            prev_zeros, prev_ones = prefix[-1]
            if num:
                prefix.append((prev_zeros, prev_ones + 1))
            else:
                prefix.append((prev_zeros + 1, prev_ones))

        res = 0

        for right in range(len(prefix)):
            for left in range(right):
                zeros = prefix[right][0] - prefix[left][0]
                ones = prefix[right][1] - prefix[left][1]

                if zeros == ones:
                    res = max(res, zeros + ones)

        return res


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list
            A: prefix sum, iteration
        """
        # One over zero surplus list.
        prefix = [0]
        # One over zero surplus counter.
        ones_counter = 0
        # One over zero surplus: index of first occurence.
        counter_index = {}

        for index, num in enumerate(nums):
            prev_ones = prefix[-1]
            if num:
                prefix.append(prev_ones + 1)
                ones_counter += 1
            else:
                prefix.append(prev_ones - 1)
                ones_counter -= 1

            if ones_counter not in counter_index:
                counter_index[ones_counter] = index

        res = 0

        for index, ones_counter in enumerate(prefix):
            if ones_counter == 0:
                res = max(res, index)
            elif ones_counter in counter_index:
                res = max(res, index - counter_index[ones_counter] - 1)

        return res


class Solution:
    def findMaxLength(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        # memo = {}

        def dfs(index, zeros, ones):
            if index == len(numbers):
                return zeros + ones if zeros == ones else 0
            # elif zeros == ones and (index, zeros) in memo:
            #     return memo[(index, zeros)]

            number = numbers[index]

            # take
            take = dfs(index + 1, zeros + (number == 0), ones + (number == 1))
            # start
            start = dfs(index + 1, 0, 0)
            # end
            end = zeros + ones if zeros == ones else 0

            # memo[(index, zeros)] = max(take, start, end)
            # return memo[(index, zeros)]
            return max(take, start, end)

        return dfs(0, 0, 0)


print(Solution().findMaxLength([0, 1]) == 2)
print(Solution().findMaxLength([0, 1, 0]) == 2)
print(Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6)
print(Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 10)
print(Solution().findMaxLength([0, 1, 1]) == 2)
print(Solution().findMaxLength([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) == 94)
print(Solution().findMaxLength([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) == 94)
