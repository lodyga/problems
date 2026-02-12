class Solution:
    def frequencySort(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(62): uppercase + lowercase + digits.
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sorting, counting sort
        """
        letter_freq = {}
        bucket = {}
        res = []

        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter, freq in letter_freq.items():
            if freq not in bucket:
                bucket[freq] = []

            bucket[freq].append(letter)

        for freq in sorted(bucket.keys(), reverse=True):
            for letter in bucket[freq]:
                res.append(letter * freq)

        return "".join(res)


class Solution:
    def frequencySort(self, text: str) -> str:
        """
        Time complexity: O(n)
            O(62): uppercase + lowercase + digits.
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sorting, bucket sort
        """
        letter_freq = {}
        bucket = {}
        res = []

        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter, freq in letter_freq.items():
            if freq not in bucket:
                bucket[freq] = []

            bucket[freq].append(letter)

        for freq in range(len(text), 0, -1):
            if freq in bucket:
                for letter in bucket[freq]:
                    res.append(letter * freq)

        return "".join(res)


print(Solution().frequencySort("tree") in ("eetr", "eert"))
print(Solution().frequencySort("cccaaa") in ("cccaaa", "aaaccc"))
print(Solution().frequencySort("Aabb") in ("bbAa", "bbaA"))
