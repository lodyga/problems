class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        Time complexity: O(n2)
            O(w * c):
            w: word count
            c: avg char count
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: iteration
        """
        counter = 0

        char_freq = [0] * 26
        for char in chars:
            index = ord(char) - ord("a")
            char_freq[index] += 1
        
        for word in words:
            char_freq_copy = char_freq.copy()
            counter += len(word)
            
            for letter in word:
                index = ord(letter) - ord("a")
                if char_freq_copy[index] == 0:
                    counter -= len(word)
                    break
                char_freq_copy[index] -= 1
        
        return counter


print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6)
print(Solution().countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10)
