import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n2logn)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: heap, array (matrix)
    *     A: greedy, Dijkstra
    * @param {number[][]} heights
    * @return {number}
    */
   minimumEffortPath(heights) {
      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const dijkstra = () => {
         const minEffortHeap = new MinPriorityQueue(x => x[0]);
         minEffortHeap.enqueue([0, 0, 0]);

         while (minEffortHeap.size()) {
            const [minEffort, row, col] = minEffortHeap.dequeue();

            if (visited[row][col])
               continue
            visited[row][col] = true;

            if (row === ROWS - 1 && col === COLS - 1)
               return minEffort

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r == -1 || r == ROWS ||
                  c == -1 || c == COLS ||
                  visited[r][c]
               ) continue

               const heightDiff = Math.abs(heights[r][c] - heights[row][col]);
               const nextMinEffort = Math.max(minEffort, heightDiff);
               minEffortHeap.enqueue([nextMinEffort, r, c]);
            }
         }
      };
      return dijkstra()
   };
}


const minimumEffortPath = new Solution().minimumEffortPath;
console.log(new Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) === 2)
console.log(new Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) === 1)
console.log(new Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) === 0)
console.log(new Solution().minimumEffortPath([[10, 8], [10, 8], [1, 2], [10, 3], [1, 3], [6, 3], [5, 2]]) === 6)
