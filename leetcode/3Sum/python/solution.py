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
        triplets = []

        left = 0
        while left < len(nums) - 2:
            left_num = nums[left]

            # If left number is > 0 then triplet sum is > 0
            if left_num > 0:
                break

            # Skip duplicate left values.
            if (
                left and
                nums[left - 1] == left_num
            ):
                left += 1
                continue

            middle = left + 1
            right = len(nums) - 1

            while middle < right:
                triplet_sum = left_num + nums[middle] + nums[right]

                if triplet_sum == 0:
                    triplets.append([left_num, nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    # Skip duplicate middle values.
                    while (
                        middle < right and
                        nums[middle - 1] == nums[middle]
                    ):
                        middle += 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    middle += 1

            left += 1
        return triplets


class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        triplets = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if not triplet in triplets:
                            triplets.append(triplet)
        return triplets


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(Solution().threeSum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
print(Solution().threeSum([1, 1, -2]) == [[-2, 1, 1]])
print(Solution().threeSum([-1, 1, 1]) == [])
print(Solution().threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]])
print(Solution().threeSum([0, 0, 0]) == [[0, 0, 0]])
print(Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
