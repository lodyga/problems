class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: greedy
        """
        # bill deposit frequency: 5, 10
        change = [0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if change[0] == 0:
                    return False
                else:
                    change[0] -= 1
                    change[1] += 1
            else:
                if change[0] and change[1]:
                    change[0] -= 1
                    change[1] -= 1
                elif change[0] >= 3:
                    change[0] -= 3
                else:
                    return False
        return True


print(Solution().lemonadeChange([5, 5, 5, 10, 20]) == True)
print(Solution().lemonadeChange([5, 5, 10, 10, 20]) == False)
print(Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]) == True)
print(Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]) == False)
