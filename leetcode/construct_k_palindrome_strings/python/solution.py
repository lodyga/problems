class Solution:
    def canConstruct(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: greedy
        """
        letter_freq = {}
        even_counter = 0
        odd_counter = 0

        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter, freq in letter_freq.items():

            if freq % 2:
                even_counter += freq - 1
                odd_counter += 1

                if odd_counter > k:
                    return False
            else:
                even_counter += freq

        return odd_counter + even_counter >= k


class Solution:
    def canConstruct(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: greedy
        """
        if len(text) < k:
            return False
        
        letter_freq = {}
        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
        
        odd_counter = 0
        
        for counter in letter_freq.values():
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
print(Solution().canConstruct("qlkzenwmmnpkopu", 15) == True)
