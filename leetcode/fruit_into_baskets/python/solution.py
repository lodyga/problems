class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: sliding window
        """
        window = {}
        left = 0
        res = 0

        for right, fruit in enumerate(fruits):
            window[fruit] = window.get(fruit, 0) + 1

            while len(window) > 2:
                left_fruit = fruits[left]
                window[left_fruit] -= 1
                left += 1

                if window[left_fruit] == 0:
                    window.pop(left_fruit)

            res = max(res, right - left + 1)

        return res


print(Solution().totalFruit([1, 2, 1]) == 3)
print(Solution().totalFruit([0, 1, 2, 2]) == 3)
print(Solution().totalFruit([1, 2, 3, 2, 2]) == 4)
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5)
print(Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5)
