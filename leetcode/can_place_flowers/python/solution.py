class Solution:
    def canPlaceFlowers(self, plots: list[int], flowers_to_plant: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        if not flowers_to_plant:
            return True

        plots.extend((0, 1))  # add one empty plot at the end
        contiguous_empty_plots = 1  # add one empty plot at the beginning
        flower_plots = 0

        for index in range(len(plots)):
            if plots[index]:
                if contiguous_empty_plots > 2:
                    # 1->0; 2->0; 3->1; 4->1; 5->2; 6->2; 7->3; 8->3; 9->4; 10->4
                    flower_plots += (contiguous_empty_plots - 1) // 2
                    if flower_plots >= flowers_to_plant:
                        return True
                contiguous_empty_plots = 0
            else:
                contiguous_empty_plots += 1

        return False


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1), True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2), False)
print(Solution().canPlaceFlowers([1, 0, 0, 0], 1), True)
print(Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0), True)
print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1), True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2), True)
print(Solution().canPlaceFlowers([0, 0, 0], 2), True)