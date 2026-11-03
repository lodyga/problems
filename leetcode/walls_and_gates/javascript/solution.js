import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} grid
    * @return {void}
    */
   wallsAndGates(grid) {
      const bfs = () => {
         while (!queue.isEmpty()) {
            const [row, col, distance] = queue.pop();

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r > -1 && r < ROWS
                  && c > -1 && c < COLS
                  && grid[r][c] === Infinity
               ) {
                  queue.push([r, c, distance + 1]);
                  grid[r][c] = distance + 1;
               }
            }
         }
      };

      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const queue = new Queue();

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col] === 0) {
               queue.push([row, col, 0]);
            }
         }
      }

      bfs();
      // return grid;
   }
}


const wallsAndGates = new Solution().wallsAndGates;
console.log(JSON.stringify(new Solution().wallsAndGates([[0, -1], [Infinity, Infinity]])) === JSON.stringify([[0, -1], [1, 2]]))
console.log(JSON.stringify(new Solution().wallsAndGates([[Infinity, Infinity, Infinity], [Infinity, -1, Infinity], [0, Infinity, Infinity]])) === JSON.stringify([[2, 3, 4], [1, -1, 3], [0, 1, 2]]))
console.log(JSON.stringify(new Solution().wallsAndGates([[Infinity, -1, 0, Infinity], [Infinity, Infinity, Infinity, -1], [Infinity, -1, Infinity, -1], [0, -1, Infinity, Infinity]])) === JSON.stringify([[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]))
