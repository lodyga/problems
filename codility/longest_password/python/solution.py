class Solution:
    def longest_password(self, passwords: str):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        def has_even_letters(word: str) -> bool:
            return sum(True for char in word if char.isalpha()) % 2 == 0

        def has_odd_digits(word: str) -> bool:
            return sum(True for char in word if char.isdigit()) % 2 == 1

        def is_alnum(word: str) -> bool:
            for char in word:
                if not char.isalnum():
                    return False
            return True


        password_length = -1
        for password in passwords.split(" "):
            if (
                is_alnum(password) and
                has_even_letters(password) and
                has_odd_digits(password)
            ):
                password_length = max(password_length, len(password))

        return password_length


print(Solution().longest_password("test 5 a0A pass007 ?xy1") == 7)
