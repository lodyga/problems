class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        balls = 0
        left_prefix = [0] * len(boxes)
        for index in range(1, len(boxes)):
            balls += 1 if boxes[index - 1] == "1" else 0
            left_prefix[index] = left_prefix[index - 1] + balls

        balls = 0
        right_prefix = [0] * len(boxes)
        for index in reversed(range(len(boxes) - 1)):
            balls += 1 if boxes[index + 1] == "1" else 0
            right_prefix[index] = right_prefix[index + 1] + balls
            left_prefix[index] += right_prefix[index]

        return left_prefix


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: prefix sum
        """
        balls = 0
        left_prefix = [0] * len(boxes)
        for index in range(1, len(boxes)):
            balls += 1 if boxes[index - 1] == "1" else 0
            left_prefix[index] = left_prefix[index - 1] + balls

        balls = 1 if boxes[-1] == "1" else 0
        right_prefix = 1 if boxes[-1] == "1" else 0
        for index in reversed(range(len(boxes) - 1)):
            left_prefix[index] += right_prefix
            balls += 1 if boxes[index] == "1" else 0
            right_prefix += balls

        return left_prefix


print(Solution().minOperations("110") == [1, 1, 3])
print(Solution().minOperations("001011") == [11, 8, 5, 4, 3, 4])
