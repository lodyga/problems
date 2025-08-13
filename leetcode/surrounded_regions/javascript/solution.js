class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: backtracking, dfs, recursion, matrix, graph
    * @param {string[][]} board
    * @return {void} Do not return anything, modify board in-place instead.
    */
   solve(board) {
      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      const dfs = (row, col) => {
         if (
            row < 0 ||
            col < 0 ||
            row === ROWS ||
            col === COLS ||
            board[row][col] !== 'O'
         ) return

         board[row][col] = '@';
         for (const [r, c] of DIRECTIONS) {
            dfs(row + r, col + c);
         }
      }

      for (let row = 0; row < ROWS; row++) {
         dfs(row, 0);
         dfs(row, COLS - 1);
      }

      for (let col = 0; col < COLS; col++) {
         dfs(0, col);
         dfs(ROWS - 1, col);
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (board[row][col] === 'O') {
               board[row][col] = 'X';
            }
         }
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (board[row][col] === '@') {
               board[row][col] = 'O';
            }
         }
      }
      
      return board
   };
}
const solve = new Solution().solve;


console.log(new Solution().solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]), [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']])
console.log(new Solution().solve([['X']]), [['X']])
console.log(new Solution().solve([['O']]), [['O']])