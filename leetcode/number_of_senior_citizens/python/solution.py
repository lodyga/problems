class Solution:
    def countSeniors(self, details: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = 0
        for detail in details:
            if (
                detail[-4] in "789" or 
                detail[-4] == "6" and detail[-3] > "0"
            ):
                counter += 1
        return counter


print(Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]) == 2)
print(Solution().countSeniors(["1313579440F2036", "2921522980M5644"]) == 0)
print(Solution().countSeniors(["9751302862F0693", "3888560693F7262", "5485983835F0649", "2580974299F6042", "9976672161M6561", "0234451011F8013", "4294552179O6482"]) == 4)
