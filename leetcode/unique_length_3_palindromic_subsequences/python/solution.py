class Solution:
    def countPalindromicSubsequence(self, text: str) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
            A: iteration
        """
        palindrome_set = set()

        for index, letter in enumerate(text):
            for left in range(index):
                left_letter = text[left]

                for right in range(index + 1, len(text)):
                    right_letter = text[right]

                    if left_letter == right_letter:
                        palindrome_set.add(left_letter + letter + right_letter)

        return len(palindrome_set)


class Solution:
    def countPalindromicSubsequence(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        palindrome_set = set()
        left_letters = set()
        right_letters = {}

        for letter in text:
            right_letters[letter] = right_letters.get(letter, 0) + 1

        for middle_letter in text:
            right_letters[middle_letter] -= 1

            if right_letters[middle_letter] == 0:
                right_letters.pop(middle_letter)

            for i in range(26):
                letter = chr(ord("a") + i)

                if (
                    letter in left_letters and
                    letter in right_letters
                ):
                    palindrome_set.add(letter + middle_letter)

            left_letters.add(middle_letter)

        return len(palindrome_set)


print(Solution().countPalindromicSubsequence("aabca") == 3)
print(Solution().countPalindromicSubsequence("adc") == 0)
print(Solution().countPalindromicSubsequence("bbcbaba") == 4)
print(Solution().countPalindromicSubsequence("zqpppgacudvmqekmefkzyyfrffeylqrwxlupvskyonqsbclwwgnzbktzelwuhehxrxmqcnepxokialxxwciqsetcsqcsszpeobeiwwedtbisyhexyatammupmfrllpawhqvfebjdappicczehrsooztjatixvtvbmdwikffbozncspuslwgoqypmsmvwghfdmutfpkbjufqrgbhotcikoyvfvxmmadelwxmvybnoroapixubdvijnepeduiwshcwjvhnejafcnuxeimwiiucznzfakwdibwwixcttatqffhnurhecyocoohyuoeixobaxbjcksxqrljiftvcxtocusciqtmydxgjexiwimbcmvhjonkscobhlpggembfslzoisertsvcpiclikprpviqbfdptvtrlhqlfwhurxysxzppnwwbxzaozchalpqsklfedovjkhwdaqdxrzdduwxsyqllvkflamtshyoaamjpzcsnwthnnpgqrrroppxnalxoijzhesphugqporhtamdbugqhgtpxtrjeugenazzpvvtkjrsepvbgvbmmmyxgrkgnlhujinycnjvpqhhugplrgrunrziaabknrjsgaqbpxfpdycpjtquecehrblzurruguhbkzgvebzfkqcolpclgabsuamqaakdikasumksvbfjrudnzihbzqjwivthfozrhkcrmxleaazgkuqmzvzaiiskfrnywntgbtmaxqgqaqxvcpvbvcpqbfivtkdroizfbebhtejegpduqjewcaysphsumddhlgerpspcvhkoezzqwznmqfbcdvxmexbjfgqxlcbneanbglpktxfcfgkfxbpblfpejlfjhiaohcmktfheuyxpof") == 676)
