class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bit manipulation, prefix sum
        """
        N = len(nums)
        prefix = [0]
        res = 0

        for num in nums:
            prefix.append(prefix[-1] ^ num)

        for k in range(N):
            for j in range(k + 1):
                for i in range(j):
                    # if prefix[i] ^ prefix[j] == prefix[k + 1] ^ prefix[j]:
                    if prefix[i] == prefix[k + 1]:
                        res += 1

        return res


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bit manipulation, prefix sum
        """
        N = len(nums)
        prefix = [0]
        res = 0

        for num in nums:
            prefix.append(prefix[-1] ^ num)

        for right in range(N + 1):
            for left in range(right):
                if prefix[left] == prefix[right]:
                    res += right - left - 1

        return res


print(Solution().countTriplets([2, 3, 1, 6, 7]) == 4)
print(Solution().countTriplets([1, 1, 1, 1, 1]) == 10)
print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]) == 8)
