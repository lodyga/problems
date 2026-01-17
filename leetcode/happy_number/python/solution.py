class Solution:
    def isHappy(self, num: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(logn)
        Tags:
            DS: hash set
            A: iteration
        """
        def sum_of_squares(num):
            next_num = 0
            while num:
                next_num += (num % 10) ** 2
                num //= 10
            return next_num

        prev_nums = set()

        while num not in prev_nums:
            prev_nums.add(num)
            next_num = sum_of_squares(num)

            if next_num == 1:
                return True
            num = next_num

        return False


class Solution:
    def isHappy(self, num: int) -> bool:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash set
            A: two pointers, Floyd
        """
        def sum_of_squares(num):
            next_num = 0
            while num:
                next_num += (num % 10) ** 2
                num //= 10
            return next_num

        slow = num
        fast = sum_of_squares(num)

        while slow != 1 and fast != 1:
            if slow == fast:
                return False

            slow = sum_of_squares(slow)
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)

        return True


print(Solution().isHappy(19) == True)
print(Solution().isHappy(2) == False)
print(Solution().isHappy(7) == True)
print(Solution().isHappy(100) == True)
print(Solution().isHappy(101) == False)
print(Solution().isHappy(1) == True)
