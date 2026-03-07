import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: dfs, recursion
    * @param {string[]} grid
    * @return {number}
    */
   regionsBySlashes(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS * 3 }, () => Array(COLS * 3).fill(false));
      let counter = 0

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            const char = grid[row][col];

            if (char === '\\') {
               for (let i = 0; i < 3; i++) {
                  visited[row * 3 + i][col * 3 + i] = true;
               }
            }

            if (char === '/') {
               for (let i = 0; i < 3; i++) {
                  visited[row * 3 + i][col * 3 + (2 - i)] = true;
               }
            }
         }
      }

      const dfs = (row, col) => {
         if (
            row === -1 || row === ROWS * 3 ||
            col === -1 || col === COLS * 3 ||
            visited[row][col]
         ) return

         visited[row][col] = true;

         for (const [dr, dc] of DIRECTIONS) {
            dfs(row + dr, col + dc);
         }

      };

      for (let row = 0; row < ROWS * 3; row++) {
         for (let col = 0; col < COLS * 3; col++) {
            if (!visited[row][col]) {
               dfs(row, col)
               counter++;
            }
         }
      }

      return counter
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {string[]} grid
    * @return {number}
    */
   regionsBySlashes(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS * 3 }, () => Array(COLS * 3).fill(false));
      let counter = 0

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            const char = grid[row][col];

            if (char === '\\') {
               for (let i = 0; i < 3; i++) {
                  visited[row * 3 + i][col * 3 + i] = true;
               }
            }

            if (char === '/') {
               for (let i = 0; i < 3; i++) {
                  visited[row * 3 + i][col * 3 + (2 - i)] = true;
               }
            }
         }
      }

      const bfs = (row, col) => {
         const queue = new Queue([[row, col]])
         visited[row][col] = true;

         while (queue.size()) {
            const [row, col] = queue.dequeue();

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r === -1 || r === ROWS * 3 ||
                  c === -1 || c === COLS * 3 ||
                  visited[r][c]
               ) continue

               queue.enqueue([r, c]);
               visited[r][c] = true;
            }

         }
      };

      for (let row = 0; row < ROWS * 3; row++) {
         for (let col = 0; col < COLS * 3; col++) {
            if (!visited[row][col]) {
               bfs(row, col)
               counter++;
            }
         }
      }

      return counter
   };
}

const regionsBySlashes = new Solution().regionsBySlashes;
console.log(new Solution().regionsBySlashes([' /', '/ ']) === 2)
console.log(new Solution().regionsBySlashes([' /', '  ']) === 1)
console.log(new Solution().regionsBySlashes(['/\\', '\\/']) === 5)
