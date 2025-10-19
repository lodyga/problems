class Solution:
    def frequencySort(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bucket sort with hash map
        """
        letter_frequency = {}
        for letter in text:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

        buckets = {}
        for key, val in letter_frequency.items():
            if val not in buckets:
                buckets[val] = set()
            buckets[val].add(key)

        sorted_text = []
        for frequency in reversed(range(1, len(text) + 1)):
            if frequency in buckets:
                for letter in buckets[frequency]:
                    sorted_text.append(letter * frequency)

        return "".join(sorted_text)


class Solution:
    def frequencySort(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bucket sort with array
        """
        letter_frequency = {}
        max_frequency = 0
        for letter in text:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
            max_frequency = max(max_frequency, letter_frequency[letter])

        buckets = [set() for _ in range(max_frequency)]
        
        for key, val in letter_frequency.items():
            buckets[val - 1].add(key)

        sorted_text = []
        for frequency in reversed(range(len(buckets))):
            if buckets[frequency]:
                for letter in buckets[frequency]:
                    sorted_text.append(letter * (frequency + 1))

        return "".join(sorted_text)


print(Solution().frequencySort("tree") == "eetr")
print(Solution().frequencySort("cccaaa") == "cccaaa")
print(Solution().frequencySort("Aabb") == "bbAa")