class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: prefix sum
        """
        N = len(boxes)
        nums = [1 if box == "1" else 0 for box in boxes]
        prefix = [0]
        suffix = [0]
        balls = 0

        for index in range(1, N):
            balls += nums[index - 1]
            prefix.append(prefix[-1] + balls)

        balls = 0

        for index in range(N - 2, -1, -1):
            balls += nums[index + 1]
            suffix.append(suffix[-1] + balls)

        suffix.reverse()
        return [prefix[index] + suffix[index] for index in range(N)]


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: prefix sum
        """
        N = len(boxes)
        prefix = [0]
        suffix = 0
        balls = 0

        for index in range(1, N):
            balls += 1 if boxes[index - 1] == "1" else 0
            prefix.append(prefix[-1] + balls)

        balls = 0

        for index in range(N - 2, -1, -1):
            balls += 1 if boxes[index + 1] == "1" else 0
            suffix += balls
            prefix[index] += suffix

        return prefix


print(Solution().minOperations("110") == [1, 1, 3])
print(Solution().minOperations("001011") == [11, 8, 5, 4, 3, 4])
