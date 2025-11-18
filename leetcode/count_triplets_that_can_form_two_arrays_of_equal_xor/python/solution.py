class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags: prefix sum, prefix xor
        """
        N = len(nums)
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] ^ num)
        
        counter = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j, N):
                    # if nums[i: j] == nums[j: k + 1]:
                    if prefix[j] ^ prefix[i] == prefix[k + 1] ^ prefix[j]:
                        counter += 1
        
        return counter


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: prefix sum, prefix xor
        """
        N = len(nums)
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] ^ num)
        
        counter = 0
        for i in range(N):
            for k in range(i + 1, N):
                if prefix[k + 1] ^ prefix[i] == 0:
                    counter += k - i
        
        return counter


print(Solution().countTriplets([2, 3, 1, 6, 7]) == 4)
print(Solution().countTriplets([1, 1, 1, 1, 1]) == 10)
