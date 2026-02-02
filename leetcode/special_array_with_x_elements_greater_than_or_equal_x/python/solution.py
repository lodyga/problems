class Solution:
    def specialArray(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        def count(mid):
            for index, num in enumerate(nums):
                if num >= mid:
                    return N - index
            return 0

        def count_bs(mid_num_to_find):
            if nums[-1] < mid_num_to_find:
                return 0
            left = 0
            right = N - 1
            res = 0
            
            while left <= right:
                mid = (left + right) // 2
                mid_num = nums[mid]
                
                if mid_num_to_find <= mid_num:
                    right = mid - 1
                    res = mid
                else:
                    left = mid + 1
            
            return len(nums) - res

        N = len(nums)
        nums.sort()
        left = 1
        right = N

        while left <= right:
            mid = (left + right) // 2
            counter = count_bs(mid)

            if counter == mid:
                return counter
            elif counter < mid:
                right = mid - 1
            else:
                left = mid + 1

        return -1


print(Solution().specialArray([3, 5]) == 2)
print(Solution().specialArray([0, 0]) == -1)
print(Solution().specialArray([0, 4, 3, 0, 4]) == 3)
print(Solution().specialArray([3, 6, 7, 7, 0]) == -1)
