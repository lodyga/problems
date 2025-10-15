class Solution:
    def intersection(self, numbers1: list[int], numbers2: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        return list(set(numbers1) & set(numbers2))


class Solution:
    def intersection(self, numbers1: list[int], numbers2: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        numbers1_set = set(numbers1)
        intersect = []
        for number in numbers2:
            if number in numbers1_set:
                intersect.append(number)
                numbers1_set.remove(number)
        return intersect


print(Solution().intersection([1, 2, 2, 1], [2, 2]) == [2])
print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9])