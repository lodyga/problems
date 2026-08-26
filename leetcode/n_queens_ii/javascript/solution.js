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
      
      const backtrack = (row) => {
         if (row === ROWS) {
            return 1;
         }

         let res = 0;

         for (let col = 0; col < COLS; col++) {
            if (
               visitedCols[col]
               || visitedDiags[row + col]
               || visitedADiags[row - col + n]
            ) {
               continue;
            }

            visitedCols[col] = true;
            visitedDiags[row + col] = true;
            visitedADiags[row - col + n] = true;

            res += backtrack(row + 1);

            visitedCols[col] = false;
            visitedDiags[row + col] = false;
            visitedADiags[row - col + n] = false;
         }

         return res;
      };

      const ROWS = n;
      const COLS = n;
      const visitedCols = Array(COLS).fill(false);
      const visitedDiags = Array(ROWS + COLS).fill(false);
      const visitedADiags = Array(ROWS + COLS).fill(false);

      return backtrack(0);
   };
}


const totalNQueens = new Solution().totalNQueens;
console.log(new Solution().totalNQueens(1) === 1)
console.log(new Solution().totalNQueens(2) === 0)
console.log(new Solution().totalNQueens(3) === 0)
console.log(new Solution().totalNQueens(4) === 2)
console.log(new Solution().totalNQueens(5) === 10)
