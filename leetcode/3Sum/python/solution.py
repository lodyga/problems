class Solution:
    def threeSum(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        triplet_list = []

        for index, number in enumerate(numbers[:-2]):
            # Skip positive numbers
            if number > 0:
                break
            # Skip same number values
            elif index and number == numbers[index - 1]:
                continue

            left = index + 1
            right = len(numbers) - 1

            while left < right:
                triplet = number + numbers[left] + numbers[right]

                if triplet == 0:
                    triplet_list.append([number, numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    # skip same left pointer values
                    while (left < right and 
                           numbers[left] == numbers[left - 1]):
                        left += 1
                    
                elif triplet > 0:
                    right -= 1
                else:
                    left += 1
            
        return triplet_list


class Solution:
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