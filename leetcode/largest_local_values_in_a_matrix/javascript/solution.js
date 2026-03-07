class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} grid
    * @return {}
    */
   largestLocal(grid) {
      const [ROWS, COLS] = [grid.length - 2, grid[0].length - 2];
      const res = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            let m = 0;

            for (let r = row; r < row + 3; r++) {
               for (let c = col; c < col + 3; c++) {
                  m = Math.max(m, grid[r][c]);
               }
            }

            res[row][col] = m;
         }
      }
      return res
   };
}


const largestLocal = new Solution().largestLocal;
console.log(new Solution().largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]).toString() === [[9, 9], [8, 6]].toString())
console.log(new Solution().largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]).toString() === [[2, 2, 2], [2, 2, 2], [2, 2, 2]].toString())
