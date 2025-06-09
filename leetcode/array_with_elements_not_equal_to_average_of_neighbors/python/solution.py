class Solution:
    def rearrangeArray(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        rear = [0] * len(numbers)
        middle = len(numbers) // 2
        left = 0
        right = middle
        index = 0
        while right < len(numbers):
            rear[index] = numbers[right]
            index += 1
            right += 1
            
            if left != middle:
                rear[index] = numbers[left]
                left += 1
                index += 1

        return rear



print(Solution().rearrangeArray([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])
print(Solution().rearrangeArray([1, 2, 3, 4]), [1, 4, 2, 3])
print(Solution().rearrangeArray([6, 2, 0, 9, 7]), [0, 9, 2, 7, 6])
print(Solution().rearrangeArray([1, 3, 2]), [1, 3, 2])
print(Solution().rearrangeArray([15, 7, 13, 6, 3, 11, 14, 1, 20]), [11, 1, 13, 3, 14, 6, 15, 7, 20])


# O(nlogn), O(n)
# slice
class Solution:
    def rearrangeArray(self, numbers: list[int]) -> list[int]:
        numbers.sort()
        length = len(numbers)
        new_numbers = [0] * length

        new_numbers[: length + 1 :2] = numbers[:(length + 1) // 2]
        new_numbers[1: length + 1 :2] = numbers[(length + 1) // 2 :]

        return new_numbers