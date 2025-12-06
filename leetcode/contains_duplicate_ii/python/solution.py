class Solution:
    def containsNearbyDuplicate(self, numbers: list[int], window_length) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window has set
        """
        window_length = min(window_length, len(numbers) - 1)
        number_count = set()

        for index, number in enumerate(numbers):
            number_count.add(number)

            if index >= window_length:
                if len(number_count) <= window_length:
                    return True
                else:
                    left_number = numbers[index - window_length]
                    number_count.discard(left_number)

        return False


class Solution:
    def containsNearbyDuplicate(self, numbers: list[int], window_length) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window as hash map
        """
        window_length = min(window_length, len(numbers) - 1)
        number_count = {}

        for index, number in enumerate(numbers):
            number_count[number] = number_count.get(number, 0) + 1

            if index >= window_length:
                if len(number_count) <= window_length:
                    return True

                left_number = numbers[index - window_length]
                number_count[left_number] -= 1

                if number_count[left_number] == 0:
                    number_count.pop(left_number)

        return False


class Solution:
    def containsNearbyDuplicate(self, numbers: list[int], window_length: int) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        window_length = window_length if window_length < len(
            numbers) - 1 else len(numbers) - 1
        for index in range(len(numbers) - window_length):
            subarray = numbers[index: index + window_length + 1]
            if len(subarray) != len(set(subarray)):
                return True

        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) == True)
print(Solution().containsNearbyDuplicate([7, 8, 9, 9], 3) == True)
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) == True)
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False)
print(Solution().containsNearbyDuplicate([99, 99], 2) == True)
print(Solution().containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3) == True)
