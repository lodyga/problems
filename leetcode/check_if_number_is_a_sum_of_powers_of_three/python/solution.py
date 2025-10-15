class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Time complexity: O(logn)
            O(log(3)n)
        Auxiliary space complexity: O(logn)
        Tags: greedy
        """
        powers = [1]
        index = 0
        while powers[-1] * 3 <= n:
            index += 1
            powers.append(3**index)
        
        for power in reversed(powers):
            if n - power >= 0:
                n -= power
            if n == 0:
                return True
        
        return False


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags: brute-force
        """
        powers = [1]
        index = 0
        while powers[-1] * 3 <= n:
            index += 1
            powers.append(3**index)
        powers.reverse()

        def dfs(index, n):
            if n < 0:
                return False
            elif n == 0:
                return True
            elif index == len(powers):
                return False
            
            # subtract
            take = dfs(index + 1, n - powers[index])
            # skip subtraction
            skip = False
            if not take:
                skip = dfs(index + 1, n)

            return take or skip

        return dfs(0, n)
        

print(Solution().checkPowersOfThree(12) == True)  # 12 = 3**1 + 3**2
print(Solution().checkPowersOfThree(91) == True)  # 91 = 3**0 + 3**2 + 3**4
print(Solution().checkPowersOfThree(21) == False)
print(Solution().checkPowersOfThree(27) == True)  # 27 = 3**3