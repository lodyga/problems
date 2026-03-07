class Solution:
    def xorQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n+q)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bit manipulation, prefix sum
        """
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] ^ num)

        return [prefix[end + 1] ^ prefix[start] 
                for start, end in queries]


print(Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]) == [2, 7, 14, 8])
print(Solution().xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]) == [8, 0, 4, 4])
