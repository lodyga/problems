class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        """
        Time complexity: O(n*k)
            n: words length
            k: avg word length
        Auxiliary space complexity: O(n*k)
        Tags: 
            DS: hash map
            A: iteration
        """
        def get_hash(word):
            hash = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                hash[index] += 1
            return tuple(hash)

        anagram_frequency = {}
        for word in words:
            key = get_hash(word)
            if key not in anagram_frequency:
                anagram_frequency[key] = []
            anagram_frequency[key].append(word)

        return list(anagram_frequency.values())


class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        """
        Time complexity: O(n*klogk)
            n: words length
            k: avg word length
        Auxiliary space complexity: O(n*k)
        Tags: 
            DS: hash map
            A: sorting
        """
        anagram_frequency = {}
        for word in words:
            key = tuple(sorted(word))
            if key not in anagram_frequency:
                anagram_frequency[key] = []
            anagram_frequency[key].append(word)

        return list(anagram_frequency.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(Solution().groupAnagrams([""]) == [[""]])
print(Solution().groupAnagrams(["a"]) == [["a"]])
print(Solution().groupAnagrams(["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]) == [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']])
print(Solution().groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]) == [["bdddddddddd"], ["bbbbbbbbbbc"]])
