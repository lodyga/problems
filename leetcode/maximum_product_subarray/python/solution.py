class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        max_product = numbers[0]
        cache = (1, 1)

        for number in numbers:
            triplet = (
                number,
                cache[0] * number,
                cache[1] * number
            )
            cache = (max(triplet), min(triplet))
            max_product = max(max_product, cache[0])

        return max_product


class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        max_product = numbers[0]
        cache = [None] * (len(numbers) + 1)
        cache[0] = (1, 1)

        for index, number in enumerate(numbers):
            triplet = (
                number,
                cache[index][0] * number,
                cache[index][1] * number
            )
            cache[index + 1] = (max(triplet), min(triplet))
            max_product = max(max_product, cache[index + 1][0])

        return max_product


class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down
        """
        self.max_product = numbers[0]

        def dfs(index):
            if index == len(numbers):
                return (1, 1)

            next_dfs = dfs(index + 1)
            triplet = (next_dfs[0] * numbers[index],
                       next_dfs[1] * numbers[index],
                       numbers[index])

            current_max = max(triplet)
            self.max_product = max(self.max_product, current_max)

            return (current_max, min(triplet))

        return max(max(dfs(0)), self.max_product)


class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        max_product = numbers[0]

        for left in range(len(numbers)):
            val = 1
            for right in range(left + 1, len(numbers)):
                val *= numbers[right]
                max_product = max(max_product, val)

        return max_product


print(Solution().maxProduct([-2]), -2)
print(Solution().maxProduct([-4, -3]), 12)
print(Solution().maxProduct([2, 3, -2, 4]), 6)
print(Solution().maxProduct([-2, 0, -1]), 0)
print(Solution().maxProduct([-2, -3, 7]), 42)
print(Solution().maxProduct([2, -5, -2, -4, 3]), 24)
print(Solution().maxProduct([0]), 0)
print(Solution().maxProduct([-2, 0]), 0)
print(Solution().maxProduct([0, 2]), 2)