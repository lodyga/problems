class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: hash map
            A: math, iteration
        """
        prod_counter = {}
        res = 0

        for right in range(len(nums)):
            num_r = nums[right]
            
            for left in range(right):
                num_l = nums[left]
                prod = num_l * num_r
                prod_counter[prod] = prod_counter.get(prod, 0) + 1

        for counter in prod_counter.values():
            # Arithmetic series.
            total = (1 + (counter - 1)) * (counter - 1) // 2
            tuple_count = total * 8
            res += tuple_count

        return res


print(Solution().tupleSameProduct([2, 3, 4, 6]) == 8)
print(Solution().tupleSameProduct([1, 2, 4, 5, 10]) == 16)
print(Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]) == 40)
print(Solution().tupleSameProduct([10, 5, 15, 8, 6, 12, 20, 4]) == 72)
print(Solution().tupleSameProduct([30, 28, 20, 6, 24, 3, 12, 14, 2, 1]) == 72)
