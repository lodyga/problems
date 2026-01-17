import heapq


class Solution:
    def reorganizeString(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: text length
            k: unique letter count
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap
            A: iteration
        """
        letter_freq = {}
        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        letter_heap = []
        for letter, freq in letter_freq.items():
            heapq.heappush(letter_heap, (-freq, letter))

        new_str = []
        while letter_heap:
            freq, letter = heapq.heappop(letter_heap)

            if new_str and letter == new_str[-1]:
                if letter_heap:
                    freq2, letter2 = heapq.heappop(letter_heap)
                    new_str.append(letter2)
                    if freq2 + 1 < 0:
                        heapq.heappush(letter_heap, (freq2 + 1, letter2))
                    heapq.heappush(letter_heap, (freq, letter))
                else:
                    return ""
            else:
                new_str.append(letter)
                if freq + 1 < 0:
                    heapq.heappush(letter_heap, (freq + 1, letter))

        return "".join(new_str)


class Solution:
    def reorganizeString(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: text length
            k: unique letter count
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap
            A: iteration
        """
        letter_freq = {}
        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        letter_heap = []
        for letter, freq in letter_freq.items():
            heapq.heappush(letter_heap, (-freq, letter))

        new_str = []
        prev_freq = 0
        prev_letter = ""
        while letter_heap:
            freq, letter = heapq.heappop(letter_heap)

            if prev_freq:
                heapq.heappush(letter_heap, (prev_freq, prev_letter))

            new_str.append(letter)
            prev_letter = letter
            prev_freq = freq + 1

        return "".join(new_str) if prev_freq == 0 else ""


print(Solution().reorganizeString("aab") == "aba")
print(Solution().reorganizeString("aaab") == "")
print(Solution().reorganizeString("kkkkzrkatkwpkkkktrq") == "krktkakpkqkrktkwkzk")
