class Solution:
    def groupAnagrams(self, word_list: list[str]) -> list[list[str]]:
        """
        Time complexity: O(n*k)
            n: list length
            k: avg word length
        Auxiliary space complexity: O(n*k)
        Tags: hash map
        """
        grouped_anagrams = {}

        for word in word_list:
            letter_bucket = [0] * 26
            for letter in word:
                letter_bucket[ord(letter) - ord("a")] += 1
            key = tuple(letter_bucket)

            if key not in grouped_anagrams:
                grouped_anagrams[key] = []
            grouped_anagrams[key].append(word)

        return list(grouped_anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(Solution().groupAnagrams([""]) == [[""]])
print(Solution().groupAnagrams(["a"]) == [["a"]])
print(Solution().groupAnagrams(["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]) == [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']])
print(Solution().groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]) == [["bdddddddddd"], ["bbbbbbbbbbc"]])