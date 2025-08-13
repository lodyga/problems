import heapq


class Solution:
    def reorganizeString(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: text.length
            k: unique_chars.count
        Auxiliary space complexity: O(1)
        Tags: heap
        """
        letter_frequency: dict = {}  # {letter: frequency, ...}
        letter_heap: list = []  # [[frequency, letter], ...]
        reorganized_string: list = []

        for letter in text:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
        
        for letter, frequency in letter_frequency.items():
            heapq.heappush(letter_heap, [-frequency, letter])

        prev_letter: str = ""
        prev_frequency: int = 0
        while letter_heap:
            frequency, letter = heapq.heappop(letter_heap)
            if prev_frequency:
                heapq.heappush(letter_heap, [prev_frequency, prev_letter])
            frequency += 1
            reorganized_string.append(letter)
            prev_letter: str = letter
            prev_frequency: int = frequency

        return "" if prev_frequency else "".join(reorganized_string)


print(Solution().reorganizeString("aab") == "aba")
print(Solution().reorganizeString("aaab") == "")
print(Solution().reorganizeString("kkkkzrkatkwpkkkktrq") == "krktkakpkqkrktkwkzk")