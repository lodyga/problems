class Solution:
    def minHeightShelves(self, books: list[list[int]], shelf_width: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        UPPER_BOUND = 10**6
        def dfs(index, shelf_width_left, shelf_height, bookshelf_height):
            if index == len(books):
                return bookshelf_height + shelf_height
        
            thickness, height = books[index]
            # if not a first book on the shelf skip current shelf
            skip = UPPER_BOUND
            if shelf_width_left != shelf_width:
                skip = dfs(index, shelf_width, 0, bookshelf_height + shelf_height)
            # check shelf width and add a book
            take = UPPER_BOUND
            if shelf_width_left >= thickness:
                take = dfs(index + 1, shelf_width_left - thickness, max(shelf_height, height), bookshelf_height)
            
            return min(skip, take)

        return dfs(0, shelf_width, 0, 0)


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelf_width: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n3)
        Tags: dp, top-down with memoization as hash map
        Fails 7th leetcode testcase.
        """
        # mimimal hight to fill bookshelf with all the remaining books
        # on particular shelf with width left
        memo = {}  # {(shefl index, book index, shelf width left): bookshelf_height, }
        UPPER_BOUND = 10**6


        def dfs(index, shelf_width_left, shelf_height, bookshelf_height, shelf_index):
            if index == len(books):
                return bookshelf_height + shelf_height
            elif (index, shelf_index, shelf_width_left) in memo:
                return memo[(index, shelf_index, shelf_width_left)]
        
            thickness, height = books[index]
            # if not a first book on the shelf skip current shelf
            skip = UPPER_BOUND
            if shelf_width_left != shelf_width:
                skip = dfs(index, shelf_width, 0, bookshelf_height + shelf_height, shelf_index + 1)
            # check shelf width and add a book
            take = UPPER_BOUND
            if shelf_width_left >= thickness:
                take = dfs(index + 1, shelf_width_left - thickness, max(shelf_height, height), bookshelf_height, shelf_index)

            memo[(index, shelf_index, shelf_width_left)] = min(skip, take)
            return memo[(index, shelf_index, shelf_width_left)]

        return dfs(0, shelf_width, 0, 0, 0)


print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4), 6)
print(Solution().minHeightShelves([[1, 3], [2, 4], [3, 2]], 6), 4)
print(Solution().minHeightShelves([[7, 3], [8, 7], [2, 7], [2, 5]], 10), 15)