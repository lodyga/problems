class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """
        Time complexity: O((n+m) * l)
            n: word1 length
            m: word2 length
            l: avg word length
        Auxiliary space complexity: O(1)
        Tags:
            DS: array, string
            A: iteration
        """
        def get_letter_freq(word):
            letter_freq = [0] * 26

            for letter in word:
                index = ord(letter) - ord("a")
                letter_freq[index] += 1

            return letter_freq

        pattren = [0] * 26
        res = []

        for word in words2:
            letter_freq = get_letter_freq(word)

            for index in range(26):
                pattren[index] = max(pattren[index], letter_freq[index])
        
        for word in words1:
            letter_freq = get_letter_freq(word)
            res.append(word)

            for index in range(26):
                if letter_freq[index] < pattren[index]:
                    res.pop()
                    break

        return res


print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]) == sorted(["facebook", "google", "leetcode"]))
print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lc", "eo"]) == sorted(["leetcode"]))
print(Solution().wordSubsets(["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], ["c", "cc", "b"]) == sorted(["cccbb"]))
