class Solution:
    def isPalindrome(self, num: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            iteration
        """
        if num < 0:
            return False

        num_copy = num
        rev_num = 0

        while num:
            rev_num = rev_num * 10 + num % 10
            num //= 10

        return num_copy == rev_num


class Solution:
    def isPalindrome(self, num: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: two pointers
        """
        str_num = str(num)
        N = len(str_num)

        for left in range(N // 2):
            right = N - 1 - left
            if str_num[left] != str_num[right]:
                return False

        return True


print(Solution().isPalindrome(121) == True)
print(Solution().isPalindrome(-121) == False)
print(Solution().isPalindrome(10) == False)
print(Solution().isPalindrome(0) == True)
