import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: heap
        """
        abc_heap = []
        happy_string = ""

        for frequency, letter in ((a, "a"), (b, "b"), (c, "c")):
            if frequency:
                heapq.heappush(abc_heap, (-frequency, letter))

        prev = (0, "")
        while abc_heap:
            frequency, letter = heapq.heappop(abc_heap)
            if prev[0]:
                heapq.heappush(abc_heap, prev)

            if (
                frequency == -1 or 
                frequency > prev[0]
            ):
                happy_string += letter
                frequency += 1
            else:
                happy_string += 2*letter
                frequency += 2

            prev = (frequency, letter) if frequency else (0, "")
        
        return happy_string


print(Solution().longestDiverseString(1, 1, 7) == "ccaccbcc")
print(Solution().longestDiverseString(7, 1, 0) == "aabaa")
print(Solution().longestDiverseString(6, 1, 1) == "aabaacaa")
print(Solution().longestDiverseString(6, 2, 0) == "aabaabaa")