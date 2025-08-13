class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n2)
    * Tags: backtracking
    * @param {number} n
    * @return {string[][]}
    */
   solveNQueens(n) {
      const rows = n;
      const cols = n;
      const board = Array.from({ length: rows }, () => Array(cols).fill('.'));
      const boardList = [];
      const visitedCols = new Set();
      const visitedDiag = new Set();
      const visitedADiag = new Set();

      const dfs = (row) => {
         if (row === rows) {
            boardList.push(board.map(row => row.join('')));  // ['.', 'Q', '.', '.'] => ['.Q..']
            return
         }

         for (let col = 0; col < cols; col++) {
            if (
               visitedCols.has(col) ||
               visitedDiag.has(row + col) ||
               visitedADiag.has(row - col)
            ) {
               continue
            }
            visitedCols.add(col);
            visitedDiag.add(row + col);
            visitedADiag.add(row - col);
            board[row][col] = 'Q';
            dfs(row + 1);
            visitedCols.delete(col);
            visitedDiag.delete(row + col);
            visitedADiag.delete(row - col);
            board[row][col] = '.';
         }
      }
      dfs(0);
      return boardList
   };
}


console.log(new Solution().solveNQueens(1), [["Q"]])
console.log(new Solution().solveNQueens(2), [])
console.log(new Solution().solveNQueens(3), [])
console.log(new Solution().solveNQueens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
console.log(new Solution().solveNQueens(5), [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."], [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."], ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."], ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."], ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]])