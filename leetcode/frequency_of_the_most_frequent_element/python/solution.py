class Solution:
    def maxFrequency(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        numbers.sort()
        left = 0
        window_sum = 0
        max_frequency = 1

        for right, number in enumerate(numbers):
            window_sum += number

            while (right - left + 1) * number - window_sum > k:
                window_sum -= numbers[left]
                left += 1

            max_frequency = max(max_frequency, right - left + 1)

        return max_frequency


print(Solution().maxFrequency([1, 2, 4], 5) == 3)
print(Solution().maxFrequency([1, 4, 8, 13], 5) == 2)
print(Solution().maxFrequency([3, 9, 6], 2) == 1)
print(Solution().maxFrequency([9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907, 9913, 9916, 9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925, 9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917, 9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966], 3056) == 73)