class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bit manipulation
        """
        # return bin(int(a, 2) + int(b, 2))[2:]
        a = a[::-1]
        b = b[::-1]
        bin_sum = ""
        carry = "0"
        
        for index in range(max(len(a), len(b))):
            char_a = a[index] if index < len(a) else "0"
            char_b = b[index] if index < len(b) else "0"
            if carry == "0":
                if char_a == "0" and char_b == "0":
                    bin_number = "0"
                    carry = "0"
                elif char_a == "0" and char_b == "1":
                    bin_number = "1"
                    carry = "0"
                elif char_a == "1" and char_b == "0":
                    bin_number = "1"
                    carry = "0"
                else:
                    bin_number = "0"
                    carry = "1"
            else:
                if char_a == "0" and char_b == "0":
                    bin_number = "1"
                    carry = "0"
                elif char_a == "0" and char_b == "1":
                    bin_number = "0"
                    carry = "1"
                elif char_a == "1" and char_b == "0":
                    bin_number = "0"
                    carry = "1"
                else:
                    bin_number = "1"
                    carry = "1"

            bin_sum += bin_number
            
        if carry == "1":
            bin_sum += "1"

        return bin_sum[::-1]


print(Solution().addBinary("11", "1") == "100")
print(Solution().addBinary("1010", "1011") == "10101")
print(Solution().addBinary("11", "11") == "110")