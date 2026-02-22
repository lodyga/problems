class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(2^k)
        Tags:
            DS: array
            A: bit manipulation, Rabin-Karp, rolling hash
        """
        codes = [False] * (1 << k)
        code_counter = 0
        window = 0
        left = 0

        for right, letter in enumerate(text):
            window <<= 1
            window += 1 if letter == "1" else 0

            if right < k - 1:
                continue

            if codes[window] is False:
                codes[window] = True
                code_counter += 1
                if code_counter == 1 << k:
                    return True

            left_num = 1 if text[left] == "1" else 0
            window -= left_num << k - 1
            left += 1

        return False


class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(2^k)
        Tags:
            DS: hash set
            A: bit manipulation, Rabin-Karp, rolling hash
        """
        code_set = set()
        window = 0
        left = 0

        for right, letter in enumerate(text):
            window <<= 1
            window += 1 if letter == "1" else 0

            if right < k - 1:
                continue

            code_set.add(window)

            if len(code_set) == 1 << k:
                return True

            left_num = 1 if text[left] == "1" else 0
            window -= left_num << k - 1
            left += 1

        return False


class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(2^k)
        Tags:
            DS: hash set
        """
        code_set = set()

        for index in range(len(text) - k + 1):
            code_set.add(text[index: index + k])

            if len(code_set) == (1 << k):
                return True

        return False


print(Solution().hasAllCodes("00110110", 2) == True)
print(Solution().hasAllCodes("0110", 1) == True)
print(Solution().hasAllCodes("0110", 2) == False)
print(Solution().hasAllCodes("00110", 2) == True)
print(Solution().hasAllCodes("0", 20) == False)
print(Solution().hasAllCodes("000011010111011001001111111001000100100100010100101100001101101101110001100100101111100111001001111001001010111010010101101001001110011100110101001001001000000110101001010011101100110110100010000", 7) == False)
