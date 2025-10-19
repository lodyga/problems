import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, queue, graph, matrix
    * @param {number[][]} grid
    * @return {number}
    */
   maxDistance(grid) {
      const ROWS = grid.length
      const COLS = grid[0].length

      if (grid.every(row => row.every(cell => cell === 0)))
         return -1
      else if (grid.every(row => row.every(cell => cell === 1)))
         return -1

      // if (Math.max(...grid.map(row => Math.max(...row))) === 0)
      //    return -1
      // let gridSum = 0;
      // for (const row of grid) {
      //    gridSum += row.reduce((total, value) => total + value, 0)
      // };
      // if (gridSum === ROWS * COLS)
      //    return -1

      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
      const queue = new Queue();
      let lastDistance = 0;

      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (grid[row][col]) {
               queue.enqueue([row, col]);
               grid[row][col] = -1;
            }

      const bfs = () => {
         let distance = 0;
         while (!queue.isEmpty()) {
            const queueLenght = queue.size();
            for (let index = 0; index < queueLenght; index++) {
               const [row, col] = queue.dequeue();
               lastDistance = distance;

               for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
                  if (
                     r === -1 ||
                     r === ROWS ||
                     c === -1 ||
                     c === COLS ||
                     grid[r][c] !== 0
                  )
                     continue

                  queue.enqueue([r, c]);
                  grid[r][c] = distance + 1;
               }
            }
            distance += 1
         }
      }

      bfs()
      return lastDistance
   };
}

const maxDistance = new Solution().maxDistance;
console.log(new Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) === 2)
console.log(new Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) === 4)
console.log(new Solution().maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) === -1)
console.log(new Solution().maxDistance([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) === -1)