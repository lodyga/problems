class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: strging
            A: iteration
        """
        res = ""

        for idx in range(len(num) - 2):
            if (
                num[idx] == num[idx + 1] == num[idx + 2]
                and (
                    res == ""
                    or res[0] < num[idx]
                )
            ):
                res = num[idx]*3

        return res


print(Solution().largestGoodInteger("6777133339") == "777")
print(Solution().largestGoodInteger("2300019") == "000")
print(Solution().largestGoodInteger("42352338") == "")
print(Solution().largestGoodInteger("333666") == "666")
print(Solution().largestGoodInteger("7678222622241118390785777474281834906756431393782326744172075725179542796491876218340") == "777")
