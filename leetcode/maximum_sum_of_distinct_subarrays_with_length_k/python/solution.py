class Solution:
    def maximumSubarraySum(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags: sliding window
        """
        left = 0
        window_map = {}
        window_sum = 0
        max_window = 0

        for right, number in enumerate(numbers):
            window_map[number] = window_map.get(number, 0) + 1
            window_sum += number

            if right - left + 1 < k:
                continue

            if len(window_map) == k:
                max_window = max(max_window, window_sum)
            
            left_number = numbers[left]
            window_map[left_number] -= 1
            if window_map[left_number] == 0:
                window_map.pop(left_number)
            window_sum -= left_number
            left += 1

        return max_window


class Solution:
    def maximumSubarraySum(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags: sliding window
        """
        self.left = 0
        window_map = {}
        self.window_sum = 0
        self.max_window = 0

        def pop_left():
            left_number = numbers[self.left]
            window_map[left_number] -= 1
            if window_map[left_number] == 0:
                window_map.pop(left_number)
            self.window_sum -= left_number
            self.left += 1


        for right, number in enumerate(numbers):
            window_map[number] = window_map.get(number, 0) + 1
            self.window_sum += number

            if right - self.left + 1 < k:
                continue

            if len(window_map) == k:
                self.max_window = max(self.max_window, self.window_sum)
            
            pop_left()
            # pop left repeated values
            while right - self.left + 1 > len(window_map):
                pop_left()

        return self.max_window



print(Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15)
print(Solution().maximumSubarraySum([4, 4, 4], 3) == 0)
print(Solution().maximumSubarraySum([9, 9, 9, 1, 2, 3], 3) == 12)
print(Solution().maximumSubarraySum([1, 5, 4, 2, 4, 1, 3], 4) == 12)