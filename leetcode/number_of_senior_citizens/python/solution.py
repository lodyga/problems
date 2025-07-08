class Solution:
    def countSeniors(self, details: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        senior_counter = 0
        
        for detail in details:
            digit1 = detail[-4]
            digit2 = detail[-3]

            if (
                digit1 > "6" or
                (digit1 == "6" and digit2 > "0")
            ):
                senior_counter += 1

        return senior_counter


print(Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]) == 2)
print(Solution().countSeniors(["1313579440F2036", "2921522980M5644"]) == 0)