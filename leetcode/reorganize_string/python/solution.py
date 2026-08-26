import heapq


class Solution:
    def reorganizeString(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: text length
            k: unique letter count
        Auxiliary space complexity: O(k)
            O(k) -> (1)
        Tags:
            DS: heap, array, string
            A: iteration
        """
        freqs = [0] * 26
        freq_heap = []
        prev_letter = ""
        prev_freq = 0
        res = []

        for letter in text:
            idx = ord(letter) - ord('a')
            freqs[idx] += 1

        for idx, freq in enumerate(freqs):
            if freq:
                heapq.heappush(freq_heap, (-freq, chr(ord('a') + idx)))


        while freq_heap:
            freq, letter = heapq.heappop(freq_heap)
            res.append(letter)

            if prev_freq:
                heapq.heappush(freq_heap, (prev_freq, prev_letter))

            prev_letter = letter
            prev_freq = freq + 1

        if prev_freq == 0:
            return "".join(res)
        else:
            return ""


class Solution:
    def reorganizeString(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: text length
            k: unique letter count
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap, hash map, string
            A: iteration
        """
        letter_freq = {}
        freq_heap = []
        res = []
        prev_letter = ""
        prev_freq = 0

        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter, freq in letter_freq.items():
            heapq.heappush(freq_heap, (-freq, letter))

        while freq_heap:
            freq, letter = heapq.heappop(freq_heap)
            res.append(letter)

            if prev_freq:
                heapq.heappush(freq_heap, (prev_freq, prev_letter))

            prev_letter = letter
            prev_freq = freq + 1

        return "".join(res) if prev_freq == 0 else ""


print(Solution().reorganizeString("aab") == "aba")
print(Solution().reorganizeString("aaab") == "")
print(Solution().reorganizeString("kkkkzrkatkwpkkkktrq") == "krktkakpkqkrktkwkzk")
