class Solution:
    def minDeletions(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        letter_frequency = [0] * 26
        for letter in text:
            index = ord(letter) - ord("a")
            letter_frequency[index] += 1

        unique_frequencies = set()
        delete_counter = 0
        for frequency in letter_frequency:
            while frequency and frequency in unique_frequencies:
                frequency -= 1
                delete_counter += 1
            unique_frequencies.add(frequency)
        
        return delete_counter


class Solution:
    def minDeletions(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bucket sort
        """
        letter_frequency = [0] * len(text)
        for letter in text:
            index = ord(letter) - ord("a")
            letter_frequency[index] += 1
        
        buckets = {}
        for frequency in letter_frequency:
            buckets[frequency] = buckets.get(frequency, 0) + 1
        
        delete_counter = 0
        for frequency in reversed(range(1, len(text) + 1)):
            if (
                frequency in buckets and 
                buckets[frequency] > 1
            ):
                diff = buckets[frequency] - 1
                buckets[frequency - 1] = buckets.get(frequency - 1, 0) + diff
                delete_counter += diff
        
        return delete_counter


print(Solution().minDeletions("aab") == 0)
print(Solution().minDeletions("aaabbbcc") == 2)
print(Solution().minDeletions("ceabaacb") == 2)