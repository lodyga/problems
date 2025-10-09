import { MinPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n2logn2)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, heap, graph, matrix
    * Dijkstra's alg
    * @param {number[][]} heights
    * @return {number}
    */
   minimumEffortPath(heights) {
      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const heightHeap = new MinPriorityQueue(x => x[0]);

      const bfs = () => {
         heightHeap.enqueue([0, 0, 0, 0]);

         while (!heightHeap.isEmpty()) {
            const [_, minEffort, row, col] = heightHeap.dequeue();
            if (row === ROWS - 1 && col === COLS - 1)
               return minEffort
            else if (visited[row][col])
               continue
            visited[row][col] = true;

            for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
               if (
                  r > -1 &&
                  r < ROWS &&
                  c > -1 &&
                  c < COLS &&
                  !visited[r][c]
               ) {
                  const heightDifference = Math.abs(heights[r][c] - heights[row][col]);
                  const newEffort = Math.max(minEffort, heightDifference);
                  heightHeap.enqueue([heightDifference, newEffort, r, c])
               }
            }
         }
      };
      return bfs()
   };
}


const minimumEffortPath = new Solution().minimumEffortPath;
console.log(new Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) === 2)
console.log(new Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) === 1)
console.log(new Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) === 0)
console.log(new Solution().minimumEffortPath([[10, 8], [10, 8], [1, 2], [10, 3], [1, 3], [6, 3], [5, 2]]) === 6)