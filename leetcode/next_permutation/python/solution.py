class Solution:
    def nextPermutation(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        n = len(numbers) - 1
        
        # Step 1: find pivot
        pivot = n - 1
        while (
            pivot > -1 and 
            numbers[pivot] >= numbers[pivot + 1]
        ):
            pivot -= 1

        # Step 2: find rightmost successor
        if pivot > -1:
            index = n
            while numbers[pivot] >= numbers[index]:
                index -= 1
            numbers[pivot], numbers[index] = numbers[index], numbers[pivot]

        # Step 3: reverse the suffix
        left = pivot + 1
        right = n
        while left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

        return numbers


print(Solution().nextPermutation([1, 2, 3, 6, 5, 4]) == [1, 2, 4, 3, 5, 6])
print(Solution().nextPermutation([1, 2, 3]) == [1, 3, 2])
print(Solution().nextPermutation([3, 2, 1]) == [1, 2, 3])
print(Solution().nextPermutation([1, 1, 5]) == [1, 5, 1])
print(Solution().nextPermutation([1, 2, 3, 4]) == [1, 2, 4, 3])
print(Solution().nextPermutation([1, 3, 2, 4]) == [1, 3, 4, 2])
print(Solution().nextPermutation([1, 2, 4, 3]) == [1, 3, 2, 4])
print(Solution().nextPermutation([4, 3, 2, 1]) == [1, 2, 3, 4])
print(Solution().nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4])
print(Solution().nextPermutation([1, 3, 4, 2]) == [1, 4, 2, 3])