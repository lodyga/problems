class Solution:
    def longestPalindrome(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
        """
        res = 0
        letter_freq = {}
        is_odd = 0

        for letter in text:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter, freq in letter_freq.items():
            if freq % 2:
                res += freq - 1
                is_odd = 1
            else:
                res += freq 

        return res + is_odd


class Solution:
    def longestPalindrome(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
        """
        res = 0
        letter_set = set()

        for letter in text:
            if letter in letter_set:
                res += 2
                letter_set.discard(letter)
            else:
                letter_set.add(letter)

        return res + bool(letter_set)


print(Solution().longestPalindrome("abccccdd") == 7)
print(Solution().longestPalindrome("a") == 1)
print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth") == 983)
