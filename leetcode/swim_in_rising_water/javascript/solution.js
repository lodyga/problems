import { MinPriorityQueue } from "@datastructures-js/priority-queue"


class Solution {
   /**
    * Time complexity: O(n2logn)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, heap, graph, matrix
    * Dijkstra's alg
    * @param {number[][]} grid
    * @return {number}
    */
   swimInWater(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const waterHeap = new MinPriorityQueue((water) => water[0]);
      waterHeap.enqueue([grid[0][0], 0, 0]);
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      visited[0][0] = true;

      // bfs()
      while (!waterHeap.isEmpty()) {
         const [waterLevel, row, col] = waterHeap.dequeue();

         if (row === ROWS - 1 && col === COLS - 1)
            return waterLevel

         for (const [r, c] of DIRECTIONS) {
            const sideRow = row + r;
            const sideCol = col + c;
            if (
               sideRow > -1 &&
               sideCol > -1 &&
               sideRow < ROWS &&
               sideCol < COLS &&
               !visited[sideRow][sideCol]
            ) {
               const reachableWaterLevel = Math.max(waterLevel, grid[sideRow][sideCol]);
               waterHeap.enqueue([reachableWaterLevel, sideRow, sideCol]);
               visited[sideRow][sideCol] = true;
            }
         }

      }
      return waterLevel
   };
}


const swimInWater = new Solution().swimInWater;
console.log(new Solution().swimInWater([[0, 2], [1, 3]]) === 3)
console.log(new Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) === 16)
console.log(new Solution().swimInWater([[3, 2], [0, 1]]) === 3)