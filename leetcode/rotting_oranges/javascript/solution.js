// import { Queue } from "@datastructures-js/queue";
const { Queue } = require("@datastructures-js/queue");


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} grid
    * @return {number}
    */
   orangesRotting(grid) {
      const bfs = () => {
         let res = 0;

         while (!queue.isEmpty()) {
            const [row, col, distance] = queue.pop();
            res = Math.max(res, distance);

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  -1 < r && r < ROWS &&
                  -1 < c && c < COLS &&
                  grid[r][c] === -1
               ) {
                  queue.push([r, c, distance + 1]);
                  grid[r][c] = distance + 1;
               }
            }
         }

         return res;
      };

      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const queue = new Queue();

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col] === 2) {
               queue.push([row, col, 0]);
               grid[row][col] = 0;
            }
            else if (grid[row][col] == 1) {
               grid[row][col] = -1;
            }
         }
      }

      const res = bfs();

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col] === -1) {
               return -1;
            }
         }
      }

      return res;
   }
}


const orangesRotting = new Solution().orangesRotting;
console.log(new Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) === 4)
console.log(new Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) === -1)
console.log(new Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2)
console.log(new Solution().orangesRotting([[0, 2]]) === 0)
console.log(new Solution().orangesRotting([[0]]) === 0)
console.log(new Solution().orangesRotting([[1]]) === -1)
console.log(new Solution().orangesRotting([[0, 0, 2, 1, 0, 1], [1, 2, 1, 1, 2, 1], [2, 1, 2, 2, 2, 0], [2, 2, 1, 0, 0, 2], [2, 2, 1, 0, 2, 2], [2, 1, 1, 2, 2, 0], [2, 2, 1, 0, 1, 1], [2, 1, 2, 1, 0, 1], [2, 1, 2, 2, 2, 2]]) === 2)
