class Solution:
    def minDeletions(self, text: str) -> int:
        import heapq
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap, array
            A: iteration
        """
        letter_freq = [0] * 26
        res = 0
        freq_heap = []

        for letter in text:
            index = ord(letter) - ord("a")
            letter_freq[index] += 1

        for freq in letter_freq:
            if freq:
                heapq.heappush(freq_heap, -freq)

        prev_freq = -freq_heap[0] + 1

        while freq_heap:
            freq = -heapq.heappop(freq_heap)

            if prev_freq == freq:
                heapq.heappush(freq_heap, -prev_freq + 1)
                res += 1
            else:
                prev_freq = freq
            
            if prev_freq == 1:
                res += len(freq_heap)
                break

        return res


class Solution:
    def minDeletions(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
            A: iteration
        """
        letter_freq = [0] * 26
        
        for letter in text:
            index = ord(letter) - ord("a")
            letter_freq[index] += 1

        unique_freqs = set()
        res = 0
        
        for frequency in letter_freq:
            while frequency and frequency in unique_freqs:
                frequency -= 1
                res += 1
            
            unique_freqs.add(frequency)
        
        return res


print(Solution().minDeletions("aab") == 0)
print(Solution().minDeletions("aaabbbcc") == 2)
print(Solution().minDeletions("ceabaacb") == 2)
print(Solution().minDeletions("abcabc") == 3)
print(Solution().minDeletions("bbcebab") == 2)
