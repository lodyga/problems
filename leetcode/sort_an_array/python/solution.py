import heapq


class Solution:
    def sortArray(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap, sorting
        """
        heapq.heapify(numbers)
        sorted_numbers = []

        while numbers:
            sorted_numbers.append(heapq.heappop(numbers))

        return sorted_numbers


class Solution:
    def sortArray(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: merge sort, sorting
        """
        def merge_sort(left, right):
            if left == right:  # if pointers point only one number
                return

            divide(left, right)
            merge(left, right)

        def divide(left, right):
            middle = (left + right) // 2
            merge_sort(left, middle)
            merge_sort(middle + 1, right)

        def merge(left, right):
            middle = (left + right) // 2
            left_chunk = numbers[left: middle + 1]  # clone left chunk
            right_chunk = numbers[middle + 1: right + 1]  # colone right chunk
            index = left
            left, right = 0, 0

            while (left < len(left_chunk) and  # while numbers in left chunk and
                   right < len(right_chunk)):  # numbers in right chunk
                # if left number is less equal than right
                if left_chunk[left] <= right_chunk[right]:
                    numbers[index] = left_chunk[left]
                    left += 1
                else:
                    numbers[index] = right_chunk[right]
                    right += 1
                index += 1

            while left < len(left_chunk):  # while still numbers in left chunk
                numbers[index] = left_chunk[left]
                left += 1
                index += 1

            while right < len(right_chunk):  # while still numbers in right chunk
                numbers[index] = right_chunk[right]
                right += 1
                index += 1

        merge_sort(0, len(numbers) - 1)
        return numbers


class Solution:
    def sortArray(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: quick sort, sorting, tle
        """
        def quick_sort(left: int, right: int) -> None:
            if left >= right:
                return

            pivot = partition(left, right)
            quick_sort(left, pivot - 1)
            quick_sort(pivot + 1, right)

        def partition(left: int, end: int) -> int:
            pivot = numbers[end]
            left -= 1

            for right in range(left + 1, end):
                if numbers[right] < pivot:
                    left += 1
                    swap_numbers(left, right)

            swap_numbers(left + 1, end)
            return left + 1

        def swap_numbers(left: int, right: int) -> None:
            numbers[left], numbers[right] = numbers[right], numbers[left]

        quick_sort(0, len(numbers) - 1)
        return numbers


class Solution:
    def sortArray(self, numbers: list[int]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: insertion sort, sorting, tle
        """
        def insertionSort():
            for right in range(1, len(numbers)):
                key = numbers[right]
                left = right - 1

                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                while (left >= 0 and numbers[left] > key):
                    numbers[left + 1] = numbers[left]
                    left -= 1
                numbers[left + 1] = key

        insertionSort()
        return numbers


class Solution:
    def sortArray(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: bubble sort, sorting
        """
        def bubble_sort():
            for i in range(len(numbers) - 1):
                for j in range(len(numbers) - 1 - i):
                    if numbers[j] > numbers[j + 1]:
                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        
        bubble_sort()
        return numbers


print(Solution().sortArray([4]) == [4])
print(Solution().sortArray([5, 4]) == [4, 5])
print(Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5])
print(Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5])
print(Solution().sortArray([-2, 3, -5]) == [-5, -2, 3])
