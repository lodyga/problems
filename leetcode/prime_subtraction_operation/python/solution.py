class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n*sqrt(m))
            n: number count
            m: max number
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        def get_prime(num):
            num = max(2, num)

            while True:
                is_prime = True

                for divider in range(2, int(num**0.5) + 1):
                    if num % divider == 0:
                        is_prime = False
                        break

                if is_prime:
                    return num

                num += 1

        for index in range(len(nums) - 2, -1, -1):
            num = nums[index]
            if num < nums[index + 1]:
                continue

            min_diff = num - nums[index + 1] + 1
            min_prime = get_prime(min_diff)

            if min_prime >= num:
                return False
            else:
                nums[index] -= min_prime

        return True


print(Solution().primeSubOperation([6, 8, 11, 12]) == True)
print(Solution().primeSubOperation([4, 9, 6, 10]) == True)
print(Solution().primeSubOperation([5, 8, 3]) == False)
print(Solution().primeSubOperation([2, 2]) == False)
print(Solution().primeSubOperation([8, 19, 3, 4, 9]) == True)
print(Solution().primeSubOperation([18, 12, 14, 6]) == False)
print(Solution().primeSubOperation([4, 18, 10, 16, 3]) == False)
print(Solution().primeSubOperation([16, 8, 4]) == False)
print(Solution().primeSubOperation([6, 16, 2]) == False)
