class Solution:
    def canJump(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        steps = 1
        
        for index in range(len(numbers) - 1):
            steps = max(steps - 1, numbers[index])
            
            if steps == 0:
                return False

        return bool(steps)


class Solution2:
    def canJump(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [False] * len(numbers)
        cache[0] = True

        for index in range(len(numbers) - 1):
            if not cache[index]:
                continue

            for i2 in range(index + 1, index + numbers[index] + 1):
                if i2 < len(numbers):
                    cache[i2] = True
            
        return cache[-1]


print(Solution().canJump([2, 3, 1, 1, 4]) == True)
print(Solution().canJump([3, 2, 1, 0, 4]) == False)
print(Solution().canJump([0]) == True)
print(Solution().canJump([2, 0, 0]) == True)
print(Solution().canJump([0, 2, 3]) == False)
print(Solution().canJump([1, 0, 1, 0]) == False)