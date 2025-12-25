import heapq


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            A: sorting, build-in function, in-place method
        """
        nums.sort()
        return nums


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: heap
            A: heap, sorting
        """
        heapq.heapify(nums)
        sorted_nums = []
        while nums:
            sorted_nums.append(heapq.heappop(nums))
        return sorted_nums


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: merge sort, sorting
        """
        def merge_sort(left, right):

            if left == right:
                return
            divide(left, right)
            merge(left, right)

        def divide(left, right):
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

        def merge(left, right):
            mid = (left + right) // 2
            left_chunk = nums[left: mid + 1]
            right_chunk = nums[mid + 1: right + 1]
            index = left
            left = right = 0

            while (
                left < len(left_chunk) and
                right < len(right_chunk)
            ):
                if left_chunk[left] < right_chunk[right]:
                    nums[index] = left_chunk[left]
                    left += 1
                else:
                    nums[index] = right_chunk[right]
                    right += 1
                index += 1

            while left < len(left_chunk):
                nums[index] = left_chunk[left]
                left += 1
                index += 1

            while right < len(right_chunk):
                nums[index] = right_chunk[right]
                right += 1
                index += 1

        merge_sort(0, len(nums))
        return nums


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
            avg case: O(nlogn)
            worst case: O(n2)
        Auxiliary space complexity: O(n)
        Tags: 
            A: quick sort, sorting, in-place method
        """
        def quick_sort(left: int, right: int) -> None:
            if left >= right:
                return

            pivot = partition(left, right)
            quick_sort(left, pivot - 1)
            quick_sort(pivot + 1, right)

        def partition(left: int, end: int) -> int:
            pivot = nums[end]

            for right in range(left, end):
                if nums[right] < pivot:
                    swap_nums(left, right)
                    left += 1

            swap_nums(left, end)
            return left

        def swap_nums(left: int, right: int) -> None:
            nums[left], nums[right] = nums[right], nums[left]

        quick_sort(0, len(nums) - 1)
        return nums


class Solution:
    def sortArray(self, nums: list[int]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            A: insertion sort, sorting
        """
        def insertionSort():
            for right in range(1, len(nums)):
                key = nums[right]
                left = right - 1

                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                while left > -1 and nums[left] > key:
                    nums[left + 1] = nums[left]
                    left -= 1
                nums[left + 1] = key

        insertionSort()
        return nums


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            A: bubble sort, sorting, in-place method
        """
        def bubble_sort():
            for left in range(len(nums)):
                for right in range(left + 1, len(nums)):
                    if nums[right] < nums[left]:
                        nums[left], nums[right] = nums[right], nums[left]

        bubble_sort()
        return nums


print(Solution().sortArray([4]) == [4])
print(Solution().sortArray([5, 4]) == [4, 5])
print(Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5])
print(Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5])
print(Solution().sortArray([-2, 3, -5]) == [-5, -2, 3])
