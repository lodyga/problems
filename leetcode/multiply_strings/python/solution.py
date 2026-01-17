class Solution:
    def multiply(self, text1: str, text2: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        if text1 == "0" or text2 == "0":
            return "0"
        
        res = [0] * (len(text1) + len(text2))
        
        for index1, num1 in enumerate(reversed(text1)):
            carry = 0
            for index2, num2 in enumerate(reversed(text2)):
                num = res[index1 + index2]
                num += int(num1) * int(num2) + carry
                res[index1 + index2] = num % 10
                carry = num // 10
            if carry:
                res[index1 + index2 + 1] += carry
            
        while res[-1] == 0:
            res.pop()
        
        return "".join(map(str, reversed(res)))


class Solution:
    def multiply(self, text1: str, text2: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        if text1 == "0" or text2 == "0":
            return "0"
        
        num_list = [0] * (len(text1) + len(text2))

        for index1, digit1 in enumerate(reversed(text1)):
            for index2, digit2 in enumerate(reversed(text2)):
                num_list[index1 + index2] += int(digit1) * int(digit2)

        carry = 0
        for index, number in enumerate(num_list):
            number += carry
            carry = number // 10
            number %= 10
            num_list[index] = number
        
        while num_list[-1] == 0:
            num_list.pop()
        
        # return "".join(str(char) for char in reversed(num_list))
        return "".join(map(str, reversed(num_list)))


print(Solution().multiply("2", "3") == "6")
print(Solution().multiply("12", "34") == "408")
print(Solution().multiply("123", "456") == "56088")
print(Solution().multiply("0", "3") == "0")
