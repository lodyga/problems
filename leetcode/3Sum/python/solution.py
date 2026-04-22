class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: two pointers, sorting
        """
        nums.sort()
        res = []

        for left in range(len(nums) - 2):
            left_num = nums[left]

            if left_num > 0:
                break

            # Skip repeating sequences with repeating left number.
            if left and nums[left - 1] == left_num:
                continue

            mid = left + 1
            right = len(nums) - 1

            while mid < right:
                mid_num = nums[mid]
                right_num = nums[right]
                triplet = left_num + mid_num + right_num

                if triplet == 0:
                    res.append([left_num, mid_num, right_num])
                    mid += 1
                    right -= 1

                    # Skip repeating sequences with repeating middle number.
                    while mid < right and nums[mid] == mid_num:
                        mid += 1

                elif triplet > 0:
                    right -= 1
                else:
                    mid += 1

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
               
                        if triplet not in triplets:
                            triplets.append(triplet)
        
        return triplets


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(Solution().threeSum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
print(Solution().threeSum([1, 1, -2]) == [[-2, 1, 1]])
print(Solution().threeSum([-1, 1, 1]) == [])
print(Solution().threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]])
print(Solution().threeSum([0, 0, 0]) == [[0, 0, 0]])
print(Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
