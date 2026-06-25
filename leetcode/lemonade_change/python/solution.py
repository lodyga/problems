class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: greedy
        """
        # [5s counter, 10s counter, 20s counter]
        cashbox = [0, 0, 0]  # change

        for bill in bills:
            if bill == 5:
                cashbox[0] += 1
            elif bill == 10:
                if cashbox[0]:
                    cashbox[0] -= 1
                    cashbox[1] += 1
                else:
                    return False
            else:  # elif bill == 15:
                if cashbox[1] and cashbox[0]:
                    cashbox[1] -= 1
                    cashbox[0] -= 1
                    cashbox[2] += 1
                elif cashbox[0] >= 3:
                    cashbox[0] -= 3
                    cashbox[2] += 1
                else:
                    return False

        return True


print(Solution().lemonadeChange([5, 5, 5, 10, 20]) == True)
print(Solution().lemonadeChange([5, 5, 10, 10, 20]) == False)
print(Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]) == False)
print(Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]) == True)
