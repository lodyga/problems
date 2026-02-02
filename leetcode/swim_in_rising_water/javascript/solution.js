import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n2logn)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: heap, array (matrix)
    *     A: greedy, Dijkstra
    * @param {number[][]} grid
    * @return {number}
    */
   swimInWater(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const waterHeap = new MinPriorityQueue(water => water[0]);
      waterHeap.enqueue([grid[0][0], 0, 0]);
      let highestWaterLevel = grid[0][0];
      visited[0][0] = true;

      while (waterHeap.size()) {
         const [waterLevel, row, col] = waterHeap.dequeue();
         highestWaterLevel = Math.max(highestWaterLevel, waterLevel);

         if (row === ROWS - 1 && col === COLS - 1)
            return highestWaterLevel

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            if (
               -1 < r && r < ROWS &&
               -1 < c && c < COLS &&
               !visited[r][c]
            ) {
               waterHeap.enqueue([grid[r][c], r, c]);
               visited[r][c] = true;
            }
         }
      }
   };
}


const swimInWater = new Solution().swimInWater;
console.log(new Solution().swimInWater([[0, 2], [1, 3]]) === 3)
console.log(new Solution().swimInWater([[3, 2], [0, 1]]) === 3)
console.log(new Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) === 16)
