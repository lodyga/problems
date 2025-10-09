class Solution:
    def isPalindrome(self, number: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        str_number = str(number)
        for left in range(len(str_number) // 2):
            if str_number[left] != str_number[len(str_number) - 1 - left]:
                return False
        return True


class Solution:
    def isPalindrome(self, number: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        if number < 0:
            return False
        
        carry = number
        reversed_number = 0
        while carry > 0:
            reversed_number = reversed_number * 10 + carry % 10
            carry = carry // 10
        
        return number == reversed_number


class Solution:
    def isPalindrome(self, number: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        if number < 0:
            return False
        
        carry = number
        number_length = 1
        while carry // 10 > 0:
            carry = carry // 10
            number_length += 1
        
        carry = number
        reversed_number = 0
        power = 10 ** (number_length - 1)
        for _ in range(number_length):
            reversed_number += (carry % 10) * power
            carry = carry // 10
            power //= 10
        
        return number == reversed_number


print(Solution().isPalindrome(121) == True)
print(Solution().isPalindrome(-121) == False)
print(Solution().isPalindrome(10) == False)
print(Solution().isPalindrome(0) == True)