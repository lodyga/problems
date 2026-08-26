import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: multi-source BFS
    * @param {string[][]} board
    * @return {void}
    */
   solve(board) {
      if (board.length === 0 || board[0].length === 0) {
         return;
      }

      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const queue = new Queue();

      // Mark border regions. Change "O" to "A".
      for (let row = 0; row < ROWS; row++) {
         if (board[row][0] === 'O') {
            queue.push([row, 0]);
            board[row][0] = 'A';
         }

         if (board[row][COLS - 1] === 'O') {
            queue.push([row, COLS - 1]);
            board[row][COLS - 1] = 'A';
         }
      }

      for (let col = 1; col < COLS - 1; col++) {
         if (board[0][col] === 'O') {
            queue.push([0, col]);
            board[0][col] = 'A';
         }

         if (board[ROWS - 1][col] === 'O') {
            queue.push([ROWS - 1, col]);
            board[ROWS - 1][col] = 'A';
         }
      }

      // Mark border-connected regions.
      while (!queue.isEmpty()) {
         const [row, col] = queue.pop();

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];

            if (
               r === -1 || r === ROWS
               || c === -1 || c === COLS
               || board[r][c] !== 'O'
            ) {
               continue;
            }

            queue.push([r, c]);
            board[r][c] = 'A';
         }
      }

      // Revert border regions marking.
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (board[row][col] === 'O') {
               board[row][col] = 'X';
            }
            else if (board[row][col] === 'A') {
               board[row][col] = 'O';
            }
         }
      }
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: multi-source DFS
    * @param {string[][]} board
    * @return {void}
    */
   solve(board) {

      const dfs = (row, col) => {
         if (
            row < 0
            || col < 0
            || row === ROWS
            || col === COLS
            || board[row][col] !== 'O'
         ) {
            return;
         }

         board[row][col] = 'A';

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            dfs(r, c);
         }
      };

      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      // Mark border regions. Change 'O' to 'A'.
      for (let row = 0; row < ROWS; row++) {
         dfs(row, 0);
         dfs(row, COLS - 1);
      }

      for (let col = 1; col < COLS - 1; col++) {
         dfs(0, col);
         dfs(ROWS - 1, col);
      }

      // Revert border regions marking.
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (board[row][col] === 'O') {
               board[row][col] = 'X';
            }
            if (board[row][col] === 'A') {
               board[row][col] = 'O';
            }
         }
      }
   }
}


const solve = new Solution().solve;
console.log(new Solution().solve([['X']]).toString() === [['X']].toString())
console.log(new Solution().solve([['O']]).toString() === [['O']].toString())
console.log(new Solution().solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]).toString() === [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']].toString())
console.log(new Solution().solve([["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]]).toString() === [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]].toString())
