class Solution:
    def canConstruct(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy, hash map
        """
        if len(text) < k:
            return False
        
        letter_frequency = {}
        for letter in text:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
        
        odd_counter = 0
        for counter in letter_frequency.values():
            if counter % 2:
                odd_counter += 1
                if odd_counter > k:
                    return False

        return True


print(Solution().canConstruct("annabelle", 2) == True)
print(Solution().canConstruct("leetcode", 3) == False)
print(Solution().canConstruct("true", 4) == True)
print(Solution().canConstruct("cr", 7) == False)
print(Solution().canConstruct("aaa", 2) == True)