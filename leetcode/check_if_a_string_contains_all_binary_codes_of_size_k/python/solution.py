class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(2^k)
        Tags: hash set
        """
        seen_code = set()
        
        for index in range(len(text) - k + 1):
            seen_code.add(text[index: index + k])
            if len(seen_code) == 2**k:
                return True
        
        return False


class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(2^k)
        Tags: bit manipulation, sliding window
        """
        if k > len(text):
            return False
        
        numbers = list(map(int, list(text)))
        seen_code = [False] * 2**k
        left = 0
        number = 0
        power = 2**(k - 1)
        
        for index in range(k - 1):
            number += numbers[index] * power
            power //= 2

        counter = 0
        for right in range(k - 1, len(text)):
            number += numbers[right]
            if not seen_code[number]:
                seen_code[number] = True
                counter += 1
                if counter == 2**k:
                    return True
            number %= 2**(k-1)
            left += 1
            number <<= 1

        return False


class Solution:
    def hasAllCodes(self, text: str, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(2^k)
        Tags: bit manipulation, sliding window
        """
        if k > len(text):
            return False
        
        numbers = list(map(int, list(text)))
        seen_code = set()
        left = 0
        number = 0
        power = 2**(k - 1)
        
        for index in range(k - 1):
            number += numbers[index] * power
            power //= 2

        for right in range(k - 1, len(text)):
            number += numbers[right]
            seen_code.add(number)

            if len(seen_code) == 2**k:
                return True
            
            number %= 2**(k-1)
            left += 1
            number <<= 1

        return False


print(Solution().hasAllCodes("00110110", 2) == True)
print(Solution().hasAllCodes("0110", 1) == True)
print(Solution().hasAllCodes("0110", 2) == False)
print(Solution().hasAllCodes("00110", 2) == True)
print(Solution().hasAllCodes("0", 20) == False)