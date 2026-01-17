class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), hash set
    *     A: DFS with backtracking
    * @param {number} n
    * @return {string[][]}
    */
   solveNQueens(n) {
      const ROWS = n;
      const COLS = n;
      const board = Array.from({ length: ROWS }, () => Array(COLS).fill('.'));
      const boardList = [];
      const visitedCols = Array(COLS).fill(false);
      const visitedDiags = new Set();
      const visitedADiags = new Set();

      const backtrack = (row) => {
         if (row === ROWS) {
            boardList.push(board.map(row => row.join('')));
            return
         }

         for (let col = 0; col < COLS; col++) {
            if (
               visitedCols[col] ||
               visitedDiags.has(row + col) ||
               visitedADiags.has(row - col)
            ) {
               continue
            }
            visitedCols[col] = true;
            visitedDiags.add(row + col);
            visitedADiags.add(row - col);
            board[row][col] = 'Q';
            backtrack(row + 1);
            visitedCols[col] = false;
            visitedDiags.delete(row + col);
            visitedADiags.delete(row - col);
            board[row][col] = '.';
         }
      }
      backtrack(0);
      return boardList
   };
}


const solveNQueens = new Solution().solveNQueens;
console.log(new Solution().solveNQueens(1), [['Q']])
console.log(new Solution().solveNQueens(2), [])
console.log(new Solution().solveNQueens(3), [])
console.log(new Solution().solveNQueens(4), [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']])
console.log(new Solution().solveNQueens(5), [['Q....', '..Q..', '....Q', '.Q...', '...Q.'], ['Q....', '...Q.', '.Q...', '....Q', '..Q..'], ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'], ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'], ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'], ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']])
