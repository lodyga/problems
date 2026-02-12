class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Time complexity: O(logn)
            O(log(3)n)
        Auxiliary space complexity: O(logn)
        Tags:
            DS: list
            A: iteration
        """
        powers = []
        power = 1

        while power <= n:
            powers.append(power)
            power *= 3

        for power in reversed(powers):
            if n - power >= 0:
                n -= power
                if n == 0:
                    return True

        return False


print(Solution().checkPowersOfThree(12) == True)
print(Solution().checkPowersOfThree(91) == True)
print(Solution().checkPowersOfThree(21) == False)
print(Solution().checkPowersOfThree(27) == True)
