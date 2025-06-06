class Solution:
    def fourSum(self, numbers: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        quadruplet_list = []

        for index1 in range(len(numbers) - 3):
            if index1 and numbers[index1 - 1] == numbers[index1]:
                continue

            for index2 in range(index1 + 1, len(numbers) - 2):
                # don't sikp index2 == index1 + 1 as it is the first index
                if (index2 > index1 + 1 and numbers[index2] == numbers[index2 - 1]):
                    continue

                left = index2 + 1
                right = len(numbers) - 1

                while left < right:
                    quadruplet = (numbers[index1] + 
                                  numbers[index2] + 
                                  numbers[left] + 
                                  numbers[right])
                    
                    if quadruplet == target:
                        quadruplet_list.append([numbers[index1], 
                                                numbers[index2], 
                                                numbers[left], 
                                                numbers[right]])
                        left += 1
                        right -= 1
                        while left < right and numbers[left - 1] == numbers[left]:
                            left += 1
                    elif quadruplet < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplet_list



print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
print(Solution().fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])
print(Solution().fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])
print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11), [[-5, -4, -3, 1]])