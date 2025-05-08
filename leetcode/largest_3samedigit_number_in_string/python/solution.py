class Solution:
    def largestGoodInteger(self, number: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        triplet = ""

        for index in range(len(number) - 2):
            if number[index] == number[index + 1] == number[index + 2]:
                triplet = max(triplet, number[index:index+3])
        
        return triplet


print(Solution().largestGoodInteger("6777133339"), "777")
print(Solution().largestGoodInteger("2300019"), "000")
print(Solution().largestGoodInteger("42352338"), "")
print(Solution().largestGoodInteger("7678222622241118390785777474281834906756431393782326744172075725179542796491876218340"), "777")
print(Solution().largestGoodInteger("333666"), "666")