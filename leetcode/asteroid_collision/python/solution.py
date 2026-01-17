class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        stack = []

        for asteroid in asteroids:
            add_asteroid = True

            while (
                stack and
                stack[-1] >= 0 and
                asteroid < 0
            ):
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif asteroid + stack[-1] == 0:
                    stack.pop()
                    add_asteroid = False
                    break
                else:  # stack[-1] > abs(asteroid)
                    add_asteroid = False
                    break

            if add_asteroid:
                stack.append(asteroid)

        return stack


print(Solution().asteroidCollision([5, 10, -5]) == [5, 10])
print(Solution().asteroidCollision([8, -8]) == [])
print(Solution().asteroidCollision([10, 2, -5]) == [10])
print(Solution().asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2])
print(Solution().asteroidCollision([1, 2, -5]) == [-5])
print(Solution().asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2])
print(Solution().asteroidCollision([-2, -1, 1, -2]) == [-2, -1, -2])
print(Solution().asteroidCollision([-2, 2, 1, -2]) == [-2])
