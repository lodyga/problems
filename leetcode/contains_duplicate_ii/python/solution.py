class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: sliding window 
        """
        window = set()
        left = 0

        for index, num in enumerate(nums):
            if num in window:
                return True
            
            window.add(num)

            if index < k:
                continue

            left_num = nums[left]
            window.remove(left_num)
            left += 1

        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) == True)
print(Solution().containsNearbyDuplicate([7, 8, 9, 9], 3) == True)
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) == True)
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False)
print(Solution().containsNearbyDuplicate([99, 99], 2) == True)
print(Solution().containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3) == True)
