class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def get_len(number):
            lenght = 0
            while number > 0:
                number //= 10
                lenght += 1
            return lenght

        def save_counter(index, counter):
            counter_length = get_len(counter)
            while counter_length > 0:
                chars[index + counter_length] = str(counter % 10)
                counter //= 10
                counter_length -= 1

        left = 0
        counter = 1
        for right, char in enumerate(chars[1:], 1):
            if chars[left] == char:
                counter += 1
                save_counter(left, counter)
            else:
                left += 1 + (get_len(counter) if counter > 1 else 0)
                chars[left] = char
                counter = 1

        return chars
        return left + 1 + (get_len(counter) if counter > 1 else 0)


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]), ["a", 2, "b", 2, "c", 3, "c"])
print(Solution().compress(["a"]), ["a"])
print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), ["a", "b", 1, 2, "b", "b", "b", "b", "b", "b", "b", "b", "b"])
print(Solution().compress(["a", "a", "a", "b", "b", "a", "a"]), ["a", "3", "b", "2", "a", "2", "a"])
print(Solution().compress(["v", "r", "r", "r", "r", "r", "r", "r", "r", "r"]), ["v", "r", "9", "r", "r", "r", "r", "r", "r", "r"])
print(Solution().compress(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]), ["a", "1", "0", "0", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "an", "a", "a", "a", "a", "a", "a", "a", "a"])
