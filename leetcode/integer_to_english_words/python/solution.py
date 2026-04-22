class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        if num == 0:
            return "Zero"

        digit_name = {
            "0": ("Zero", ""),
            "1": ("One", "What?_1"),
            "2": ("Two", "Twenty"),
            "3": ("Three", "Thirty"),
            "4": ("Four", "Forty"),
            "5": ("Five", "Fifty"),
            "6": ("Six", "Sixty"),
            "7": ("Seven", "Seventy"),
            "8": ("Eight", "Eighty"),
            "9": ("Nine", "Ninety"),
            "11": ("Eleven", ),
            "12": ("Twelve", ),
            "13": ("Thirteen", ),
            "14": ("Fourteen", ),
            "15": ("Fifteen", ),
            "16": ("Sixteen", ),
            "17": ("Seventeen", ),
            "18": ("Eighteen", ),
            "19": ("Nineteen", ),
            "10": ("Ten", ),
            "20": ("Twenty", ),
            "30": ("Thirty", ),
            "40": ("Forty", ),
            "50": ("Fifty", ),
            "60": ("Sixty", ),
            "70": ("Seventy", ),
            "80": ("Eighty", ),
            "90": ("Ninety", ),

        }
        digits = []
        res = []

        while num:
            mod = num % 10
            digits.append(str(mod))
            num //= 10

        index = 0
        while index < len(digits):
            digit = digits[index]
            three_zeros = not any(digit != "0" 
                                  for digit in digits[index: index + 3])

            if three_zeros:
                index += 3
                continue

            if index % 3 == 0:
                if index == 3:
                    res.append("Thousand")
                elif index == 6:
                    res.append("Million")
                elif index == 9:
                    res.append("Billion")

                # Check for two digit number.
                if index + 1 < len(digits):
                    next_digit = digits[index + 1]
                    
                    # Is 00.
                    if digit == "0" and next_digit == "0":
                        index += 1
                        continue
                    # Starts with 1.
                    if next_digit == "1":
                        digit = next_digit + digit
                        index += 1
                    # Ends with 0.
                    elif digit == "0" and next_digit != "0":
                        digit = next_digit + digit
                        index += 1

                res.append(digit_name[digit][0])

            elif index % 3 == 1:
                res.append(digit_name[digit][1])

            elif index % 3 == 2:
                if digit != "0":
                    res.append("Hundred")
                    res.append(digit_name[digit][0])

            index += 1

        return " ".join(w for w in res[::-1] if w != "")


print(Solution().numberToWords(0) == "Zero")
print(Solution().numberToWords(10) == "Ten")
print(Solution().numberToWords(20) == "Twenty")
print(Solution().numberToWords(21) == "Twenty One")
print(Solution().numberToWords(111) == "One Hundred Eleven")
print(Solution().numberToWords(123) == "One Hundred Twenty Three")
print(Solution().numberToWords(12_345) == "Twelve Thousand Three Hundred Forty Five")
print(Solution().numberToWords(1_234_567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print(Solution().numberToWords(1_234_567_891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
print(Solution().numberToWords(100) == "One Hundred")
print(Solution().numberToWords(1000) == "One Thousand")
print(Solution().numberToWords(1001) == "One Thousand One")
print(Solution().numberToWords(1000000) == "One Million")
print(Solution().numberToWords(100000001), "One Hundred Million One")
