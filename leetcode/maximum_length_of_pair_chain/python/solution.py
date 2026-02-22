class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, greedy, sorting
        """
        pairs.sort()
        counter = 0
        prev_end = pairs[0][0] - 1

        for start, end in pairs:
            if prev_end < start:
                prev_end = end
                counter += 1

            prev_end = min(prev_end, end)

        return counter


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, greedy, sorting
        """
        pairs.sort(key=lambda pair: pair[1])
        counter = 0
        prev_end = pairs[0][0] - 1

        for start, end in pairs:
            if prev_end < start:
                counter += 1
                prev_end = end
        
        return counter


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        pairs.sort()
        lis = [1] * len(pairs)

        for right, right_pair in enumerate(pairs):
            for left in range(right):
                left_pair = pairs[left]

                if left_pair[1] < right_pair[0]:
                    lis[right] = max(lis[right], lis[left] + 1)

        return max(lis)


print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2)
print(Solution().findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3)
