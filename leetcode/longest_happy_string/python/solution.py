import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap, string
            A: greedy, iteration
        """
        letter_heap = []
        res = []
        prev_letter = ''
        prev_freq = 0

        for letter, freq in zip("abc", (a, b, c)):
            if freq:
                heapq.heappush(letter_heap, (-freq, letter))

        while letter_heap:
            freq, letter = heapq.heappop(letter_heap)

            if prev_freq:
                heapq.heappush(letter_heap, (prev_freq, prev_letter))

            # Limit current letter frequency because of previous letter with higher frequency.
            if (freq == -1 or prev_freq < freq):
                k = 1
            else:
                k = 2

            res.append(letter*k)
            prev_freq = freq + k
            prev_letter = letter

        return "".join(res)


print(Solution().longestDiverseString(1, 1, 7) == "ccaccbcc")
print(Solution().longestDiverseString(7, 1, 0) == "aabaa")
print(Solution().longestDiverseString(6, 1, 1) == "aabaacaa")
print(Solution().longestDiverseString(6, 2, 0) == "aabaabaa")
print(Solution().longestDiverseString(8, 3, 0) == "aabaabaabaa")
