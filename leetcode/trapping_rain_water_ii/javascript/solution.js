import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n2log(n2))
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: heap, array (matrix)
    *     A: greedy, multi-source Dijkstra
    * @param {number[][]} heightMap
    * @return {number}
    */
   trapRainWater(heightMap) {
      const ROWS = heightMap.length;
      const COLS = heightMap[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      // heap([[height, row, col], ])
      const heightHeap = new MinPriorityQueue(x => x[0]);

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (
               row === 0 || row === ROWS - 1 ||
               col === 0 || col === COLS - 1
            ) {
               const height = heightMap[row][col];
               heightHeap.enqueue([height, row, col]);
               visited[row][col] = true;
            }
         }
      }

      const dijkstra = () => {
         let maxHeight = 0;
         let res = 0;

         while (heightHeap.size()) {
            const [height, row, col] = heightHeap.dequeue();
            maxHeight = Math.max(maxHeight, height);
            res += maxHeight - height;

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r == -1 || r == ROWS ||
                  c == -1 || c == COLS ||
                  visited[r][c]
               )
                  continue

               heightHeap.enqueue([heightMap[r][c], r, c]);
               visited[r][c] = true;
            }

         }
         return res
      }

      return dijkstra()
   };
}


const trapRainWater = new Solution().trapRainWater;
console.log(new Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]) === 4)
console.log(new Solution().trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]) === 10)
console.log(new Solution().trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]) === 14)
