import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: queue, array (matrix)
    *     A: multi-source BFS
    * @param {number[][]} isWater
    * @return {number[][]}
    */
   highestPeak(isWater) {
      const ROWS = isWater.length;
      const COLS = isWater[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const res = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
      const queue = new Queue();

      const bfs = () => {
         let height = 0;

         while (queue.size()) {
            const queueSize = queue.size();

            for (let index = 0; index < queueSize; index++) {
               const [row, col] = queue.dequeue();

               if (res[row][col])
                  continue

               res[row][col] = height;

               for (const [dr, dc] of DIRECTIONS) {
                  const [r, c] = [row + dr, col + dc];

                  if (
                     r === -1 || r === ROWS ||
                     c === -1 || c === COLS ||
                     isWater[r][c] ||
                     res[r][c] !== 0
                  )
                     continue

                  queue.enqueue([r, c]);
               }
            }
            height += 1
         }
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (isWater[row][col])
               queue.enqueue([row, col])
         }
      }

      bfs()
      return res
   };
}

const highestPeak = new Solution().highestPeak;
console.log(new Solution().highestPeak([[0, 1], [0, 0]]).toString() === [[1, 0], [2, 1]].toString())
console.log(new Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]).toString() === [[1, 1, 0], [0, 1, 1], [1, 2, 2]].toString())
console.log(new Solution().highestPeak([[0, 0], [1, 1], [1, 0]]).toString() === [[1, 1], [0, 0], [0, 1]].toString())
