class Solution:
    def multiply(self, number1: str, number2: str) -> str:
        """
        Time complexity: O(n2)
            n: number length
        Auxiliary space complexity: O(n)
        Tags: iteration
        """
        if number1 == "0" or number2 == "0":
            return "0"
        
        number_list = [0] * (len(number1) + len(number2))
        for index1, digit1 in enumerate(reversed(number1)):
            for index2, digit2 in enumerate(reversed(number2)):
                number_list[index1 + index2] += int(digit1) * int(digit2)
                pass

        carry = 0
        index = 0
        while index < len(number_list) or carry:
            number = number_list[index] + carry
            carry = number // 10
            number_list[index] = number % 10
            index += 1

        while number_list[-1] == 0:
            number_list.pop()
        
        return "".join(reversed(list(map(str, number_list))))


print(Solution().multiply("2", "3") == "6")
print(Solution().multiply("12", "34") == "408")
print(Solution().multiply("123", "456") == "56088")
print(Solution().multiply("0", "3") == "0")