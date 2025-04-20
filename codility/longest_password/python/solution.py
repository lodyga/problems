class Solution:
    def longest_password(self, passwords: str):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        password_length = 0

        for password in passwords.split(" "):
            if (password.isalnum() and
                self.has_even_letters(password) and
                self.has_odd_digits(password) and
                    len(password) > password_length):
                password_length = len(password)

        return password_length

    def has_even_letters(self, password):
        letter_counter = 0
        for char in password:
            if char.isalpha():
                letter_counter += 1
        return not (letter_counter % 2)

    def has_odd_digits(self, password):
        digit_counter = 0
        for char in password:
            if char.isdigit():
                digit_counter += 1
        return digit_counter % 2


print(Solution().longest_password("test 5 a0A pass007 ?xy1"), 7)