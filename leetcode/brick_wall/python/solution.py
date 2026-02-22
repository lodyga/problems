class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        """
        Time complexity: O(n)
            n: brick count
        Auxiliary space complexity: O(m)
            m: distinct crack count
        Tags:
            DS: hash map
            A: prefix sum
        """
        # {crack position: vertical crack count}
        crack_freq = {0: 0}

        for brick_row in wall:
            prefix = 0
            
            for index in range(len(brick_row) - 1):
                brick = brick_row[index]
                prefix += brick
                crack_freq[prefix] = crack_freq.get(prefix, 0) + 1

        return len(wall) - max(crack_freq.values())


print(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2)
print(Solution().leastBricks([[1], [1], [1]]) == 3)
print(Solution().leastBricks([[2147483647, 2147483647, 2147483647, 2147483647]]) == 0)
print(Solution().leastBricks([[1]]) == 1)
print(Solution().leastBricks([[1000]]) == 1)
print(Solution().leastBricks([[100000000, 100000000], [100000000, 100000000]]) == 0)
print(Solution().leastBricks([[2], [2], [2]]) == 3)
