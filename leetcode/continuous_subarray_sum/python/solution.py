class Solution:
    def checkSubarraySum(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        for left in range(len(numbers)):
            total = 0
            for right in range(left, len(numbers)):
                total += numbers[right]
                if total % k == 0:
                    return True
        return False


class Solution:
    def checkSubarraySum(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(k)
        Tags: gredy, hash set, tle
        """
        number_set = set()
        for number in numbers:
            number_set = {(n + number) % k for n in number_set}
            if 0 in number_set:
                return True
            number_set.add(number % k)

        return False


class Solution:
    def checkSubarraySum(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum, hash map
        """
        prefix_mod = [0] * (len(numbers) + 1)
        for index, number in enumerate(numbers):
            prefix_mod[index + 1] = (prefix_mod[index] + number) % k
        
        # {prefix mod: index}
        # Case when prefix mod == 0, then 0 - 0, 
        # and index = -1 for case when the first element is % k == 0.
        prefix_map = {0: -1}
        for index, pre in enumerate(prefix_mod[1:]):
            if pre in prefix_map:
                if index - prefix_map[pre] > 1:
                    return True
            else:
                prefix_map[pre] = index

        return False


print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6) == True)
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) == True)
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13) == False)
print(Solution().checkSubarraySum([0], 1) == False)
print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7) == True)
print(Solution().checkSubarraySum([24], 6) == False)
