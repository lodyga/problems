class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        dna_set = set()
        dupliactes = set()
        
        for right in range(9, len(text)):
            window = text[right - 9: right + 1]
            if window in dna_set:
                dupliactes.add(window)
            else:
                dna_set.add(window)
        
        return list(dupliactes)


class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: rolling hash
        """
        letter_value = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3
        }

        rolling_hash = 0
        dna_hash_map = {}  # hash: (True: to add, False: added)
        dupliactes = set()
        base = 5
        power = base**9
        
        for index in range(len(text)):
            letter = text[index]
            rolling_hash = rolling_hash * base + letter_value[letter]

            if index < 9:
                continue

            if rolling_hash in dna_hash_map:
                if dna_hash_map[rolling_hash]:
                    dupliactes.add(text[index - 9: index + 1])
                    dna_hash_map[rolling_hash] = False
            else:
                dna_hash_map[rolling_hash] = True

            left_letter = text[index - 9]
            rolling_hash -= (letter_value[left_letter] * power)
        
        return list(dupliactes)


print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC", "CCCCCAAAAA"])
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])
print(Solution().findRepeatedDnaSequences("A"), [])
