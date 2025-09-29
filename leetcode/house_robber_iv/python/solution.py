class Solution:
    def minCapability(self, houses: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: binary search, greedy
        """        
        # dp, top-down with memoization as hash map
        def validate_capability_dfs(capability):
            memo = {}
            
            def dfs(index, houses_robbed):
                if houses_robbed >= k:
                    return True
                elif index >= len(houses):
                    return False
                elif (index, houses_robbed) in memo:
                    return memo[(index, houses_robbed)]

                # rob house
                rob_house = False
                if capability >= houses[index]:
                    rob_house = dfs(index + 2, houses_robbed + 1)
                # skip house
                skip_house = False
                if not rob_house:
                    skip_house = dfs(index + 1, houses_robbed)
                
                memo[(index, houses_robbed)] = skip_house or rob_house
                return memo[(index, houses_robbed)]

            return dfs(0, 0)

        # greedy
        def validate_capability_greedy(capability):
            index = 0
            robbed_houses = 0
            while index < len(houses):
                if houses[index] <= capability:
                    robbed_houses += 1
                    index += 2
                    if robbed_houses == k:
                        return True
                else:
                    index += 1
            return False

        sorted_capabilities = sorted(houses)
        left = 0
        right = len(sorted_capabilities) - 1
        min_capability = sorted_capabilities[right]
        
        while left <= right:
            middle = (left + right) // 2
            capability = sorted_capabilities[middle]

            if validate_capability_greedy(capability):
                min_capability = capability
                right = middle - 1
            else:
                left = middle + 1

        return min_capability


class Solution:
    def minCapability(self, houses: list[int], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        upper_bound = max(houses) + 1
        memo = {}

        def dfs(index, rob_counter):
            if rob_counter >= k:
                return 0
            elif index >= len(houses):
                return upper_bound
            elif (index, rob_counter) in memo:
                return memo[(index, rob_counter)]
        
            rob_house = max(houses[index], dfs(index + 2, rob_counter + 1))
            skip_house = dfs(index + 1, rob_counter)

            # min capability
            memo[(index, rob_counter)] = min(rob_house, skip_house)
            return memo[(index, rob_counter)]

        return dfs(0, 0)


class Solution:
    def minCapability(self, houses: list[int], k: int) -> int:
        """
        Time complexity: O(nlogm)
            n: house count
            m: capacity range; log2(10**9) = 30
        Auxiliary space complexity: O(1)
        Tags: binary search, greedy
        """
        def valid_capacity(capacity):
            index = 0
            rob_counter = 0
            while index < len(houses):
                if houses[index] <= capacity:
                    rob_counter += 1
                    index += 2
                else:
                    index += 1
                if rob_counter == k:
                    return True
            return False

        left = min(houses)
        right = max(houses)
        min_capacity = left

        while left <= right:
            middle = (left + right) // 2
            can_rob = valid_capacity(middle)

            if can_rob:
                right = middle - 1
                min_capacity = middle
            else:
                left = middle + 1

        return min_capacity


print(Solution().minCapability([2, 2], 1) == 2)
print(Solution().minCapability([1, 4, 5], 1) == 1)
print(Solution().minCapability([2, 3, 5, 9], 2) == 5)
print(Solution().minCapability([2, 7, 9, 3, 1], 2) == 2)
print(Solution().minCapability([5038, 3053, 2825, 3638, 4648, 3259, 4948, 4248, 4940, 2834, 109, 5224, 5097, 4708, 2162, 3438, 4152, 4134, 551, 3961, 2294, 3961, 1327, 2395, 1002, 763, 4296, 3147, 5069, 2156, 572, 1261, 4272, 4158, 5186, 2543, 5055, 4735, 2325, 1206, 1019, 1257, 5048, 1563, 3507, 4269, 5328, 173, 5007, 2392, 967, 2768, 86, 3401, 3667, 4406, 4487, 876, 1530, 819, 1320, 883, 1101, 5317, 2305, 89, 788, 1603, 3456, 5221, 1910, 3343, 4597], 28) == 4134)