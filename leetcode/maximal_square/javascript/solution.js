class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as array
    * @param {number[][]} matrix
    * @return {number}
    */
   maximalSquare(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      // [i, j]: max square side for i, j being top left corner
      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));

      const dfs = (row, col) => {
         if (row === ROWS || col === COLS)
            return 0
         else if (memo[row][col] !== -1)
            return memo[row][col]
         else if (matrix[row][col] === '0') {
            memo[row][col] = 0
            return 0
         }
         const side = Math.min(
            dfs(row, col + 1),
            dfs(row + 1, col),
            dfs(row + 1, col + 1)
         );
         memo[row][col] = side + 1
         return side + 1
      }

      let maxSide = 0;
      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            maxSide = Math.max(maxSide, dfs(row, col))

      return maxSide ** 2
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, bottom-up
    * @param {number[][]} matrix
    * @return {number}
    */
   maximalSquare(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      // [i, j]: max square side for i, j being top left corner
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));
      let maxSide = 0;

      for (let row = ROWS - 1; row > -1; row--)
         for (let col = COLS - 1; col > -1; col--)
            if (matrix[row][col] === '1') {

               const side = Math.min(
                  cache[row][col + 1],
                  cache[row + 1][col],
                  cache[row + 1][col + 1]
               );
               cache[row][col] = 1 + side;
               maxSide = Math.max(maxSide, 1 + side);
            }
      return maxSide ** 2
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[][]} matrix
    * @return {number}
    */
   maximalSquare(matrix) {
      const ROWS = matrix.length;
      const COLS = matrix[0].length;
      // [i, j]: max square side for i, j being top left corner
      const blankCache = Array(COLS + 1).fill(0);
      let nextCache = blankCache;
      let maxSide = 0;

      for (let row = ROWS - 1; row > -1; row--) {
         const cache = blankCache.slice();
         for (let col = COLS - 1; col > -1; col--) {
            if (matrix[row][col] === '1') {
               const side = Math.min(
                  cache[col + 1],
                  nextCache[col],
                  nextCache[col + 1]
               );
               cache[col] = 1 + side;
               maxSide = Math.max(maxSide, 1 + side);
            }
         }
         nextCache = cache.slice();
      }
      return maxSide ** 2
   };
}


const maximalSquare = new Solution().maximalSquare;
console.log(new Solution().maximalSquare([['1', '1']]) === 1)
console.log(new Solution().maximalSquare([['1', '1'], ['1', '1']]) === 4)
console.log(new Solution().maximalSquare([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]) === 4)
console.log(new Solution().maximalSquare([['0', '1'], ['1', '0']]) === 1)
console.log(new Solution().maximalSquare([['0']]) === 0)
console.log(new Solution().maximalSquare([['1', '1', '1', '1', '0'], ['1', '1', '1', '1', '0'], ['1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['0', '0', '1', '1', '1']]) === 16)