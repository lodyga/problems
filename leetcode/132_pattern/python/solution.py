class Solution:
    def find132pattern(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack, monotonic stack
        monotonic decreasing stack
        """
        stack = []
        prev_min_number = numbers[0]

        for number in numbers[1:]:
            while stack and stack[-1][1] <= number:
                stack.pop()
            
            if stack and stack[-1][0] < number:
                return True

            stack.append((prev_min_number, number))
            prev_min_number = min(prev_min_number, number)

        return False


print(Solution().find132pattern([3, 1, 4, 2]) == True)
print(Solution().find132pattern([1, 2, 3, 4]) == False)
print(Solution().find132pattern([-1, 3, 2, 0]) == True)
print(Solution().find132pattern([3, 5, 0, 3, 4]) == True)
print(Solution().find132pattern([1, 0, 1, -4, -3]) == False)
print(Solution().find132pattern([-2, 1, 2, -2, 1, 2]) == True)
print(Solution().find132pattern([1, 2, 3, 4, -4, -3, -5, -1]) == False)
print(Solution().find132pattern([1, 3, -4, 2]) == True)


# O(n2), O(1)
# tle
class Solution:
    def find132pattern(self, numbers: list[int]) -> bool:
        for right, number in enumerate(numbers[2:], 2):
            middle = right - 1

            while middle > 0:
                if numbers[middle] > number:
                    left = middle - 1

                    while left >= 0:
                        if numbers[left] < number:
                            return True

                        left -= 1

                middle -= 1

        return False


# O(n3), O(1)
# brute force
class Solution:
    def find132pattern(self, numbers: list[int]) -> bool:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    if numbers[i] < numbers[k] < numbers[j]:
                        return True
        return False