import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap
            A: greedy, iteration
        """
        letter_heap = []
        for letter, freq in zip("abc", (a, b, c)):
            if freq:
                heapq.heappush(letter_heap, (-freq, letter))

        prev_letter = ""
        prev_freq = 0
        happy_list = []
        while letter_heap:
            freq, letter = heapq.heappop(letter_heap)

            if prev_freq:
                heapq.heappush(letter_heap, (prev_freq, prev_letter))

            if (
                freq == -1 or
                # Limit current letter becouse of letter with highter frequency.
                prev_freq < freq
            ):
                happy_list.append(letter)
                prev_freq = freq + 1
                prev_letter = letter
            else:
                happy_list.append(letter*2)
                prev_freq = freq + 2
                prev_letter = letter

        return "".join(happy_list)


print(Solution().longestDiverseString(1, 1, 7) == "ccaccbcc")
print(Solution().longestDiverseString(7, 1, 0) == "aabaa")
print(Solution().longestDiverseString(6, 1, 1) == "aabaacaa")
print(Solution().longestDiverseString(6, 2, 0) == "aabaabaa")
