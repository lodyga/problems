class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        For Loop Approach 
        """
        coins.sort()
        # The number of ways to make remaining amount using coins starting from coins[index:].
        memo = {}

        def dfs(index, remaining):
            if remaining == 0:
                return 1
            elif remaining < 0:
                return 0
            elif (index, remaining) in memo:
                return memo[(index, remaining)]

            memo[(index, remaining)] = 0
            for index2 in range(index, len(coins)):
                coin = coins[index2]
                memo[(index, remaining)] += dfs(index2, remaining - coin)

            return memo[(index, remaining)]

        return dfs(0, amount)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        For Loop Approach 
        """
        coins.sort()
        # The number of ways to reach amount with already accumulated current_sum, unsing coinst strating from coins[index:].
        memo = {}

        def dfs(index, current_sum):
            if current_sum == amount:
                return 1
            elif current_sum > amount:
                return 0
            elif (index, current_sum) in memo:
                return memo[(index, current_sum)]

            memo[(index, current_sum)] = 0
            for index2 in range(index, len(coins)):
                coin = coins[index2]
                memo[(index, current_sum)] += dfs(index2, current_sum + coin)
                
            return memo[(index, current_sum)]

        return dfs(0, 0)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        Binary Decision Approach
        """
        coins.sort()
        # The number of ways to reach amount with already accumulated current_sum, unsing coinst strating from coins[index:].
        memo = {}

        def dfs(index, current_sum):
            if current_sum == amount:
                return 1
            elif (
                index == len(coins) or
                current_sum > amount
            ):
                return 0
            elif (index, current_sum) in memo:
                return memo[(index, current_sum)]

            taken = dfs(index, current_sum + coins[index])
            skipped = dfs(index + 1, current_sum)
            memo[(index, current_sum)] = taken + skipped
            return memo[(index, current_sum)]

        return dfs(0, 0)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Time complexity: O(n2)
            O(coin_length * amount)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        Binary Decision Approach
        """
        coins.sort()
        # The number of ways to make remaining amount using coins starting from coins[index:].
        memo = {}

        def dfs(index, remaining):
            if remaining == 0:
                return 1
            elif (
                index == len(coins) or
                remaining < 0
            ):
                return 0
            elif (index, remaining) in memo:
                return memo[(index, remaining)]
            
            taken = dfs(index, remaining - coins[index])
            skipped = dfs(index + 1, remaining)
            memo[(index, remaining)] = skipped + taken
            return memo[(index, remaining)]

        return dfs(0, amount)


# memo = {}  # {amount: ways to make it up}
print(Solution().change(2, [1, 2]), 2)
print(Solution().change(3, [1, 2, 3]), 3)
print(Solution().change(5, [1, 2, 5]), 4)
print(Solution().change(10, [10]), 1)
print(Solution().change(3, [2]), 0)
print(Solution().change(500, [3, 5, 7, 8, 9, 10, 11]), 35502874)
# print(Solution().change(4681, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468, 470, 472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 780, 936, 1170, 1560, 2340, 4680]), 0)