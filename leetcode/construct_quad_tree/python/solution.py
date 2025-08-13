class Node:
    """
    Definition for a QuadTree node.
    """
    
    def __init__(self, val=None, isLeaf=None, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    Time complexity: O(n2logn)
    Auxiliary space complexity: O(logn)
    Tags: tree
    """

    def construct(self, grid: list[list[int]]) -> 'Node':
        def is_leaf(row, col, n):
            for r in range(row, row + n):
                for c in range(col, col + n):
                    if grid[r][c] != grid[row][col]:
                        return False
            return True

        def dfs(row, col, n):
            if is_leaf(row, col, n):
                return Node(grid[row][col], True)
            else:
                n //= 2
                top_left = dfs(row, col, n)
                top_right = dfs(row, col + n, n)
                bottom_left = dfs(row + n, col, n)
                bottom_right = dfs(row + n, col + n, n)
                return Node(None, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, 0, len(grid))


print(Solution().construct([[0, 1], [1, 0]]), [[0,0],[1,0],[1,1],[1,1],[1,0]])
print(Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]), [[0,0],[1,1],[0,0],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]])