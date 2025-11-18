class Solution:
    def longestPalindrome(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash map
        """
        letter_frequency = {}
        for letter in text:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

        has_odd = False
        palindrome_lenght = 0

        for frequency in letter_frequency.values():
            if frequency % 2:
                has_odd = True
                palindrome_lenght += frequency - 1
            else:
                palindrome_lenght += frequency

        return palindrome_lenght + has_odd


class Solution:
    def longestPalindrome(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash set
        """
        palindrome_lenght = 0
        letter_set = set()

        for letter in text:
            if letter in letter_set:
                palindrome_lenght += 2
                letter_set.discard(letter)
            else:
                letter_set.add(letter)

        return palindrome_lenght + bool(letter_set)


print(Solution().longestPalindrome("abccccdd") == 7)
print(Solution().longestPalindrome("a") == 1)
print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth") == 983)
