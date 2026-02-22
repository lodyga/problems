class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        res = 0

        for index in range(1, len(arrays)):
            current_min = arrays[index][0]
            current_max = arrays[index][-1]
            res = max(
                res,
                current_max - global_min,
                global_max - current_min
            )
            global_min = min(global_min, current_min)
            global_max = max(global_max, current_max)

        return res


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        min_num = 10**4 + 1
        max_num = -10**4 - 1

        for index, arr in enumerate(arrays):
            if arr[0] < min_num:
                min_num = arr[0]
                min_ind = index
            if arr[-1] > max_num:
                max_num = arr[-1]
                max_ind = index

        if min_ind != max_ind:
            return max_num - min_num

        prev_min_num = min_num
        prev_min_ind = min_ind
        prev_max_num = max_num
        prev_max_ind = max_ind

        min_num = 10**4 + 1
        max_num = -10**4 - 1

        for index, arr in enumerate(arrays):
            if index != prev_min_ind and arr[0] < min_num:
                min_num = arr[0]
                min_ind = index
            if index != prev_max_ind and arr[-1] > max_num:
                max_num = arr[-1]
                max_ind = index

        return max(prev_max_num - min_num, max_num - prev_min_num)


print(Solution().maxDistance([[-10, -8, -8, -6, -4, 4], [-4, -3]]) == 8)
print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4)
print(Solution().maxDistance([[1], [1]]) == 0)
print(Solution().maxDistance([[1, 4], [0, 5]]) == 4)
