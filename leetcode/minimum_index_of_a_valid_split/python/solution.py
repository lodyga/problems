class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: bucket sort
        """
        N = len(nums)
        postfix_num_freq = {}
        prefix_num_freq = {}

        for num in nums:
            postfix_num_freq[num] = postfix_num_freq.get(num, 0) + 1

        postfix_bucket = [set() for _ in range(max(postfix_num_freq.values()))]
        prefix_bucket = []

        for num, freq in postfix_num_freq.items():
            postfix_bucket[freq - 1].add(num)

        for index in range(len(nums) - 1):
            num = nums[index]
            freq = postfix_num_freq[num]
            postfix_bucket[freq - 1].remove(num)
            postfix_num_freq[num] -= 1

            if postfix_num_freq[num] == 0:
                postfix_num_freq.pop(num)
            else:
                postfix_bucket[freq - 2].add(num)

            while postfix_bucket and len(postfix_bucket[-1]) == 0:
                postfix_bucket.pop()

            if num in prefix_num_freq:
                freq = prefix_num_freq[num]
                prefix_bucket[freq - 1].remove(num)

            prefix_num_freq[num] = prefix_num_freq.get(num, 0) + 1
            freq = prefix_num_freq[num]

            if len(prefix_bucket) < freq:
                prefix_bucket.append(set([num]))
            else:
                prefix_bucket[freq - 1].add(num)

            if len(prefix_bucket[-1]) > 1 or len(postfix_bucket[-1]) > 1:
                continue

            if (
                prefix_bucket[-1] == postfix_bucket[-1] and
                len(prefix_bucket) * 2 > (index + 1) and
                len(postfix_bucket) * 2 > (N - index - 1)
            ):
                return index

        return -1


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        N = len(nums)
        postfix_num_freq = {}
        prefix_num_freq = {}

        for num in nums:
            postfix_num_freq[num] = postfix_num_freq.get(num, 0) + 1

        for index in range(len(nums) - 1):
            num = nums[index]
            prefix_num_freq[num] = prefix_num_freq.get(num, 0) + 1
            postfix_num_freq[num] -= 1

            if (
                prefix_num_freq[num] * 2 > (index + 1) and
                postfix_num_freq[num] * 2 > (N - index - 1)
            ):
                return index

        return -1


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: voting
        """
        N = len(nums)
        major = 0
        counter = 0

        for num in nums:
            if counter == 0 or num == major:
                major = num
                counter += 1
            else:
                counter -= 1

        left_counter = 0
        right_counter = sum(True for num in nums if num == major)

        for index in range(len(nums) - 1):
            num = nums[index]

            if num == major:
                left_counter += 1
                right_counter -= 1

                if (
                    left_counter * 2 > index + 1 and
                    right_counter * 2 > N - index - 1
                ):
                    return index

        return -1


print(Solution().minimumIndex([1, 2, 2, 2]) == 2)
print(Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]) == 4)
print(Solution().minimumIndex([3, 3, 3, 3, 7, 2, 2]) == -1)
