class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: greedy, intervals, sorting
        """
        pairs.sort(key=lambda pair: pair[1])
        counter = 1
        prev_end = pairs[0][1]

        for right in range(1, len(pairs)):
            start, end = pairs[right]
            if prev_end < start:
                counter += 1
                prev_end = end
        return counter


print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2)
print(Solution().findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3)
