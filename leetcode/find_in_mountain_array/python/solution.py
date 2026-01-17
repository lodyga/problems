class MountainArray:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def get(self, index: int) -> int:
        return self.nums[index]

    def length(self) -> int:
        return len(self.nums)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: MountainArray) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search        
        """
        length = mountainArr.length()
        peak = 0
        
        # find the peak
        left = 1
        right = length - 2
        while left <= right:
            mid = (left + right) // 2
            mid_height = mountainArr.get(mid)
            left_height = mountainArr.get(mid - 1)
            right_height = mountainArr.get(mid + 1)

            if left_height < mid_height > right_height:
                peak = mid
                break
            elif mid_height < right_height:
                left = mid + 1
                peak = left
            else:
                right = mid - 1
                peak = right
        
        # search the left portion
        left = 0
        right = peak
        while left <= right:
            mid = (left + right) // 2
            mid_height = mountainArr.get(mid)

            if target == mid_height:
                return mid
            elif target < mid_height:
                right = mid - 1
            else:
                left = mid + 1

        # search the left portion
        left = peak
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            mid_height = mountainArr.get(mid)

            if target == mid_height:
                return mid
            elif target > mid_height:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1


print(Solution().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2)
print(Solution().findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])) == -1)
