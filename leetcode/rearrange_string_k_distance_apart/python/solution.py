import heapq
from collections import deque


class Solution:
    def rearrangeString(self, text: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap, queue, array
            A: iteration
        """
        num_freq = [0] * 26
        # heap([(freq, letter, avaible), ])
        top_num_heap = []
        res = []
        # deque([(freq, letter, avaible), ])
        cool_queue = deque()
        time_stamp = 1

        for letter in text:
            index = ord(letter) - ord("a")
            num_freq[index] += 1

        for index in range(26):
            if num_freq[index]:
                heapq.heappush(
                    top_num_heap,
                    (-num_freq[index], chr(index + ord("a")), 0))

        # while top_num_heap or cool_queue:
        while time_stamp <= len(text):
            while cool_queue and cool_queue[0][2] <= time_stamp:
                heapq.heappush(top_num_heap, cool_queue.popleft())

            if not top_num_heap:
                return ""

            freq, letter, _ = heapq.heappop(top_num_heap)
            res.append(letter)

            if freq < -1:
                cool_queue.append((freq + 1, letter, time_stamp + k))

            time_stamp += 1

        return "".join(res)


print(Solution().rearrangeString("aabbcc", 3) == "abcabc")
print(Solution().rearrangeString("aaabc", 3) == "")
print(Solution().rearrangeString("aaadbbcc", 2) == "abacabcd")
