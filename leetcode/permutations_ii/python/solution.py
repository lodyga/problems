class Solution:
    def permuteUnique(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n!)
        Tags: backtracking, hash set
        """
        numbers.sort()
        permutation_list = []

        def dfs(left):
            if left == len(numbers) - 1:
                permutation_list.append(tuple(numbers))
                return

            unique_level_value = set()
            for right in range(left, len(numbers)):
                if numbers[right] in unique_level_value:
                    continue
                else:
                    unique_level_value.add(numbers[right])

                numbers[left], numbers[right] = numbers[right], numbers[left]
                dfs(left + 1)
                numbers[left], numbers[right] = numbers[right], numbers[left]

        dfs(0)
        return list(permutation_list)


class Solution2:
    def permuteUnique(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n!)
        Tags: backtracking, hash map
        """
        permutation = []
        permutation_list = []
        number_frequency = {}
        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        def dfs():
            if len(permutation) == len(numbers):
                permutation_list.append(permutation.copy())
                return

            for number in number_frequency:
                if number_frequency[number] > 0:
                    permutation.append(number)
                    number_frequency[number] -= 1
                    dfs()
                    permutation.pop()
                    number_frequency[number] += 1

        dfs()
        return permutation_list


class Solution:
    def permuteUnique(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n!)
        Tags: backtracking, hash set
        """
        permutation_set = set()

        def dfs(left):
            if left == len(numbers) - 1:
                permutation_set.add(tuple(numbers))
                return

            for right in range(left, len(numbers)):
                numbers[left], numbers[right] = numbers[right], numbers[left]
                dfs(left + 1)
                numbers[left], numbers[right] = numbers[right], numbers[left]

        dfs(0)
        return list(permutation_set)


print(Solution().permuteUnique([1, 2]), [[1, 2], [2, 1]])
print(Solution().permuteUnique([1, 2, 3]), [[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]])
print(Solution().permuteUnique([1]), [[1]])
print(Solution().permuteUnique([1, 1, 2]), [[1, 2, 1], [2, 1, 1], [1, 1, 2]])
print(Solution().permuteUnique([2, 2, 1, 1]), [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]])