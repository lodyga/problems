class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        """
        Time complexity: O(n*k)
            n: words length
            k: avg word length
        Auxiliary space complexity: O(n*k)
        Tags:
            DS: hash map, list, array
            A: iteration
        """
        anagram_groups = {}

        for word in words:
            letter_freq = [0] * 26

            for letter in word:
                idx = ord(letter) - ord("a")
                letter_freq[idx] += 1
            
            key = tuple(letter_freq)
            
            if key not in anagram_groups:
                anagram_groups[key] = []
            
            anagram_groups[key].append(word)
        
        return list(anagram_groups.values())


class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        """
        Time complexity: O(n*klogk)
            n: words length
            k: avg word length
        Auxiliary space complexity: O(n*k)
        Tags:
            DS: hash map, list
            A: sorting
        """
        anagram_groups = {}
        
        for word in words:
            key = tuple(sorted(word))
        
            if key not in anagram_groups:
                anagram_groups[key] = []
        
            anagram_groups[key].append(word)

        return list(anagram_groups.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(Solution().groupAnagrams([""]) == [[""]])
print(Solution().groupAnagrams(["a"]) == [["a"]])
print(Solution().groupAnagrams(["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]) == [['tin'], ['ram'], ['zip', 'zip'], ['cry'], ['pus'], ['jon'], ['pyx']])
print(Solution().groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]) == [["bdddddddddd"], ["bbbbbbbbbbc"]])
