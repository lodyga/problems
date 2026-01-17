import { Queue } from "@datastructures-js/queue";


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
         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            dfs(r, c);
         }
      }

      // Mark border regions. Change "O" to "@".
      for (let row = 0; row < ROWS; row++) {
         dfs(row, 0);
         dfs(row, COLS - 1);
      }
      for (let col = 0; col < COLS; col++) {
         dfs(0, col);
         dfs(ROWS - 1, col);
      }

      // Capture internal regions.
      for (let row = 1; row < ROWS - 1; row++) {
         for (let col = 1; col < COLS - 1; col++) {
            if (board[row][col] === 'O') {
               board[row][col] = 'X';
            }
         }
      }

      // Revert border regions marking.
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (board[row][col] === '@') {
               board[row][col] = 'O';
            }
         }
      }

      return board
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: multi-source DFS
    * @param {string[][]} board
    * @return {void}
    */
   solve(board) {
      const ROWS = board.length;
      const COLS = board[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      const bfs = (row, col) => {
         if (board[row][col] !== 'O')
            return

         // const queue = new Queue([[row, col]]);
         const queue = [[row, col]];
         // while (queue.size()) {
         while (queue.length) {
            // const [row, col] = queue.dequeue();
            const [row, col] = queue.pop();
            board[row][col] = "@";

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r < 0 ||
                  c < 0 ||
                  r === ROWS ||
                  c === COLS ||
                  board[r][c] !== 'O'
               ) continue

               // queue.enqueue([r, c]);
               queue.push([r, c])
               board[r][c] = '@';
            }
         }

      }

      // Mark border regions. Change "O" to "@".
      for (let row = 0; row < ROWS; row++) {
         bfs(row, 0);
         bfs(row, COLS - 1);
      }
      for (let col = 0; col < COLS; col++) {
         bfs(0, col);
         bfs(ROWS - 1, col);
      }

      // Capture internal regions.
      for (let row = 1; row < ROWS - 1; row++) {
         for (let col = 1; col < COLS - 1; col++) {
            if (board[row][col] === 'O') {
               board[row][col] = 'X';
            }
         }
      }

      // Revert border regions marking.
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
console.log(new Solution().solve([['X']]).toString() === [['X']].toString())
console.log(new Solution().solve([['O']]).toString() === [['O']].toString())
console.log(new Solution().solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]).toString() === [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']].toString())
console.log(new Solution().solve([["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]]).toString() === [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]].toString())
