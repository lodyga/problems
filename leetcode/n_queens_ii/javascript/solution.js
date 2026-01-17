class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: backtracking
    * @param {number} n
    * @return {number}
    */
   totalNQueens(n) {
      const ROWS = n;
      const COLS = n;
      let counter = 0;
      const visitedCols = Array(COLS).fill(false);
      const visitedDiags = Array(ROWS + COLS - 1).fill(false);
      const visitedADiags = Array(ROWS + COLS).fill(false);

      const dfs = (row) => {
         if (row === ROWS) {
            counter++
            return
         }
         for (let col = 0; col < COLS; col++) {
            if (
               visitedCols[col] ||
               visitedDiags[row + col] ||
               visitedADiags[row - col + n]
            ) continue

            visitedCols[col] = true;
            visitedDiags[row + col] = true;
            visitedADiags[row - col + n] = true;

            dfs(row + 1);

            visitedCols[col] = false;
            visitedDiags[row + col] = false;
            visitedADiags[row - col + n] = false;
         }
      }
      dfs(0);
      return counter
   };
}


const totalNQueens = new Solution().totalNQueens;
console.log(new Solution().totalNQueens(1) === 1)
console.log(new Solution().totalNQueens(2) === 0)
console.log(new Solution().totalNQueens(3) === 0)
console.log(new Solution().totalNQueens(4) === 2)
console.log(new Solution().totalNQueens(5) === 10)
