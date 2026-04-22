class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Failed
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: sliding window
        """
        vowels = set("aeiou")

        def count_at_most(k: int) -> int:
            if k < 0:
                return 0

            vowel_freq = {}
            left = 0
            mid = 0
            cons_count = 0
            total = 0

            for right, letter in enumerate(word):
                if letter in "aeiou":
                    vowel_freq[letter] = vowel_freq.get(letter, 0) + 1
                else:
                    cons_count += 1

                if len(vowel_freq) < 5 or cons_count < k:
                    continue
                
                while cons_count == k and len(vowel_freq) == 5:
                    left_letter = word[mid]

                    if left_letter in "aeiou":
                        vowel_freq[left_letter] -= 1
                        if vowel_freq[left_letter] == 0:
                            vowel_freq.pop(left_letter)
                    else:
                        cons_count -= 1

                    mid += 1

                if len(vowel_freq) == 5 and cons_count == k:
                    total += (mid - left + 1)

            return total
        a = count_at_most(k)
        b = count_at_most(k + 1)
        
        return count_at_most(k) - count_at_most(k + 1)


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: sliding window
        """
        vowels = "aeiou"

        def count_at_most(k: int) -> int:
            if k < 0:
                return 0

            vowel_index = {v: -1 for v in vowels}
            seen = 0
            left = 0
            cons_count = 0
            res = 0

            for right, letter in enumerate(word):
                if letter in vowels:
                    if vowel_index[letter] == -1:
                        seen += 1
                    vowel_index[letter] = right
                else:
                    cons_count += 1

                while cons_count > k:
                    if word[left] not in vowels:
                        cons_count -= 1
                    left += 1

                if seen == 5:
                    first_vowel_index = min(vowel_index.values())
                    if first_vowel_index >= left:
                        res += (first_vowel_index - left + 1)

            return res

        return count_at_most(k) - count_at_most(k - 1)


print(Solution().countOfSubstrings("aeiou", 0), 1)
print(Solution().countOfSubstrings("aeioqq", 1), 0)
print(Solution().countOfSubstrings("uqaeiouq", 1), 4)
print(Solution().countOfSubstrings("ieaouqqieaouqq", 1), 3)
print(Solution().countOfSubstrings("iqeaouqi", 2), 3)
print(Solution().countOfSubstrings("iqeaouqii", 2), 5)
