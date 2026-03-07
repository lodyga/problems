class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
        """
        dna_set = set()
        repeated = set()

        for right in range(9, len(text)):
            dna = text[right - 9: right + 1]

            if dna in dna_set:
                repeated.add(dna)
            else:
                dna_set.add(dna)

        return list(repeated)


class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: Rabin-Karp, rolling hash
        """
        val = {"A": 0, "C": 1, "G": 2,  "T": 3}
        rolling_hash = 0
        # {dna hash: False(one occurence) / True (two or more occurences)}
        dna_freq = {}
        # {dna hash: dna sequence}
        dna_map = {}
        base = 4
        power = base**9

        for right, letter in enumerate(text):
            rolling_hash *= base
            rolling_hash += val[letter]

            if right < 9:
                continue

            if rolling_hash not in dna_map:
                dna_map[rolling_hash] = text[right - 9: right + 1]
                dna_freq[rolling_hash] = False
            else:
                dna_freq[rolling_hash] = True

            left_letter = text[right - 9]
            rolling_hash -= val[left_letter] * power

        return [dna_map[rolling_hash]
                for rolling_hash in dna_freq
                if dna_freq[rolling_hash]]


class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: bit manipulation
        """
        if len(text) < 10:
            return []

        val = {"A": 0, "C": 1, "G": 2, "T": 3}
        mask = (1 << 20) - 1  # keep last 20 bits

        rolling_hash = 0
        seen = set()
        repeated = set()

        for index, letter in enumerate(text):
            rolling_hash = ((rolling_hash << 2) | val[letter]) & mask

            if index < 9:
                continue
            
            if rolling_hash in seen:
                repeated.add(text[index - 9: index + 1])
            else:
                seen.add(rolling_hash)

        return list(repeated)


print(sorted(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == sorted(["AAAAACCCCC", "CCCCCAAAAA"]))
print(sorted(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")) == sorted(["AAAAAAAAAA"]))
print(sorted(Solution().findRepeatedDnaSequences("A")) == sorted([]))
