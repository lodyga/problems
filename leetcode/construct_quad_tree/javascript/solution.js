/**
 * Definition for a QuadTree node.
 */
class _Node {
   constructor(val=null, isLeaf=null, topLeft=null, topRight=null, bottomLeft=null, bottomRight=null) {
      this.val = val;
      this.isLeaf = isLeaf;
      this.topLeft = topLeft;
      this.topRight = topRight;
      this.bottomLeft = bottomLeft;
      this.bottomRight = bottomRight;
   }
};


/**
 * Time complexity: O(n2logn)
 * Auxiliary space complexity: O(logn)
 * Tags: tree
 */
class Solution {
   /**
    * Check if Node is a leaf node;
    * @param {number[][]} grid
    * @returns {boolean}
    */
   construct(grid) {
      const isLeaf = (row, col, n) => {
         for (let r = row; r < row + n; r++) {
            for (let c = col; c < col + n; c++) {
               if (grid[r][c] !== grid[row][col]) {
                  return false
               }
            }
         }
         return true
      };

      /**
       * @param {number} row 
       * @param {number} col 
       * @param {number} n 
       * @returns {Node}
       */
      const dfs = (row, col, n) => {
         if (isLeaf(row, col, n)) {
            return new Node(grid[row][col], true)
         } else {
            n /= 2;
            const topLeft = dfs(row, col, n);
            const topRight = dfs(row, col + n, n);
            const bottomLeft = dfs(row + n, col, n);
            const bottomRight = dfs(row + n, col + n, n);
            return new Node(null, false, topLeft, topRight, bottomLeft, bottomRight)
         }
      }      
      return dfs(0, 0, grid.length)
   };
}
const construct = new Solution().construct;


print(Solution().construct([[0, 1], [1, 0]]), [[0,0],[1,0],[1,1],[1,1],[1,0]])
print(Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]), [[0,0],[1,1],[0,0],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]])