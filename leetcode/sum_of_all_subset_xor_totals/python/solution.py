class Solution:
    def subsetXORSum(self, numbers: int) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        def get_xor_sum():
            if not subset:
                return 0

            xor_sum = subset[0]
            for number in subset[1:]:
                xor_sum ^= number

            return xor_sum

        subset = []
        xored_list = []

        def dfs(index):
            if index == len(numbers):
                xored_list.append(get_xor_sum())
                return

            subset.append(numbers[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return sum(xored_list)


print(Solution().subsetXORSum([1, 3]), 6)
print(Solution().subsetXORSum([5, 1, 6]), 28)
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]), 480)