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
        char_freq = [0] * 26
        res = 0

        for letter in chars:
            idx = ord(letter) - ord("a")
            char_freq[idx] += 1

        for word in words:
            char_freq_copy = char_freq.copy()
            res += len(word)

            for letter in word:
                idx = ord(letter) - ord("a")
                char_freq_copy[idx] -= 1
                
                if char_freq_copy[idx] == -1:
                    res -= len(word)
                    break

        return res


print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6)
print(Solution().countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10)
