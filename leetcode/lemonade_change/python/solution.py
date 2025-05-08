class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash map
        """
        money_counter = {
            5: 0, 
            10: 0, 
            20: 0
        }
        
        for bill in bills:
            if bill == 5:
                money_counter[5] += 1
            elif bill == 10:
                if money_counter[5] == 0:
                    return False
                else:
                    money_counter[5] -= 1
                    money_counter[10] += 1
            elif bill == 20:
                if (money_counter[10] > 0 and 
                        money_counter[5] > 0):
                    money_counter[5] -= 1
                    money_counter[10] -= 1
                elif money_counter[5] > 2:
                    money_counter[5] -= 3
                else:
                    return False
                money_counter[20] += 1
        
        return True


print(Solution().lemonadeChange([5, 5, 5, 10, 20]), True)
print(Solution().lemonadeChange([5, 5, 10, 10, 20]), False)
print(Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]), True)
print(Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]), False)
