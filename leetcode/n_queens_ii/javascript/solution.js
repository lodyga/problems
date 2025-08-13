class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number} n
    * @return {number}
    */
   totalNQueens(n) {
      const rows = n;
      const cols = n;
      let counter = 0;
      const visitedCols = new Set();
      const visitedDiags = new Set();
      const visitedAdiags = new Set();

      const dfs = (row) => {
         if (row === rows) {
            counter++
            return
         }
         for (let col = 0; col < cols; col++) {
            if (
               visitedCols.has(col) ||
               visitedDiags.has(row + col) ||
               visitedAdiags.has(row - col)
            ) continue
            
            visitedCols.add(col);
            visitedDiags.add(row + col);
            visitedAdiags.add(row - col);
            dfs(row + 1);
            visitedCols.delete(col);
            visitedDiags.delete(row + col);
            visitedAdiags.delete(row - col);
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