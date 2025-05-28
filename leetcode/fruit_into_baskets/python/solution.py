class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        window = {}
        total_fruit = 0

        for right, fruit in enumerate(fruits):
            window[fruit] = window.get(fruit, 0) + 1

            while len(window) > 2:
                left_fruit = fruits[left]
                window[left_fruit] -= 1
                if window[fruits[left]] == 0:
                    window.pop(fruits[left])
                left += 1

            total_fruit = max(total_fruit, right - left + 1)

        return total_fruit


print(Solution().totalFruit([1, 2, 1]) == 3)
print(Solution().totalFruit([0, 1, 2, 2]) == 3)
print(Solution().totalFruit([1, 2, 3, 2, 2]) == 4)
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5)
print(Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5)