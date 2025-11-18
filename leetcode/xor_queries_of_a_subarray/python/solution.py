class Solution:
    def xorQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n+q)
        Auxiliary space complexity: O(n)
        Tags: prefix sum, prefix xor
        """
        prefix = [0] * (len(nums) + 1)
        for index in range(1, len(nums) + 1):
            prefix[index] = prefix[index - 1] ^ nums[index - 1]

        response = []
        for start, end in queries:
            response.append(prefix[end + 1] ^ prefix[start])

        return response


print(Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]) == [2, 7, 14, 8])
print(Solution().xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]) == [8, 0, 4, 4])
