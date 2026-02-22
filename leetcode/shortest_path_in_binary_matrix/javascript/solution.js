import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} grid
    * @return {}
    */
   shortestPathBinaryMatrix(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      
      if (
         grid[0][0] === 1 ||
         grid[ROWS - 1][COLS - 1] === 1
      ) {
         return -1
      }

      const DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
      [0, 1], [1, -1], [1, 0], [1, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const queue = new Queue([[0, 0]]);
      visited[0][0] = true;
      let dist = 1;

      // bfs
      while (queue.size()) {
         const queueSize = queue.size();
         
         for (let _ = 0; _ < queueSize; _++) {
            const [row, col] = queue.dequeue();

            if (row === ROWS - 1 && col === COLS - 1) {
               return dist
            }

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r === -1 || r === ROWS ||
                  c === -1 || c === COLS ||
                  visited[r][c] ||
                  grid[r][c] === 1
               ) {
                  continue
               }

               queue.enqueue([r, c]);
               visited[r][c] = true;
            }

         }
         dist++;
      }

      return -1
   };
}


const shortestPathBinaryMatrix = new Solution().shortestPathBinaryMatrix;
console.log(new Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) === 2)
console.log(new Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]) === -1)
console.log(new Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) === 4)
console.log(new Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) === -1)
