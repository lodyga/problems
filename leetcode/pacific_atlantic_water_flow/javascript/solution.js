class Solution {
   /**
    * Time complexity: O(n2)
    *     n: heights length
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: multi-source DFS
    * @param {number[][]} heights
    * @return {number[][]}
    */
   pacificAtlantic(heights) {
      const dfs = (row, col, prevHeight, toOcean) => {
         if (
            row === -1 || row === ROWS
            || col === -1 || col === COLS
            || heights[row][col] < prevHeight
            || toOcean[row][col]
         ) {
            return;
         }

         toOcean[row][col] = true;

         for (const [dr, dc] of DIRECTIONS) {
            dfs(row + dr, col + dc, heights[row][col], toOcean);
         }
      };

      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const toPacific = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const toAtlantic = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const res = [];

      for (let row = 0; row < ROWS; row++) {
         dfs(row, 0, 0, toPacific);
         dfs(row, COLS - 1, 0, toAtlantic);
      }

      for (let col = 0; col < COLS; col++) {
         dfs(0, col, 0, toPacific);
         dfs(ROWS - 1, col, 0, toAtlantic)
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (toPacific[row][col] && toAtlantic[row][col]) {
               res.push([row, col]);
            }
         }
      }

      return res;
   }
}


import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    *     n: heights length
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: queue, array (matrix)
    *     A: multi-source BFS
    * @param {number[][]} heights
    * @return {number[][]}
    */
   pacificAtlantic(heights) {
      
      const bfs = (queue, toOcean) => {
         while (!queue.isEmpty()) {
            const [row, col] = queue.pop();

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r === -1 || r === ROWS
                  || c === -1 || c === COLS
                  || heights[r][c] < heights[row][col]
                  || toOcean[r][c]
               ) continue;

               queue.push([r, c]);
               toOcean[r][c] = true;
            }
         }

         // return toOcean;
      };

      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const toPacific = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const toAtlantic = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const toPacificCells = new Queue();
      const toAtlanticCells = new Queue();
      const res = [];

      for (let row = 0; row < ROWS; row++) {
         toPacificCells.push([row, 0]);
         toPacific[row][0] = true;
         toAtlanticCells.push([row, COLS - 1]);
         toAtlantic[row][COLS - 1] = true;
      }

      for (let col = 1; col < COLS; col++) {
         toPacificCells.push([0, col]);
         e
      }

      for (let col = 0; col < COLS - 1; col++) {
         toAtlanticCells.push([ROWS - 1, col]);
         toAtlantic[ROWS - 1][col] = true;
      }

      bfs(toPacificCells, toPacific);
      bfs(toAtlanticCells, toAtlantic);

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (toPacific[row][col] && toAtlantic[row][col])
               res.push([row, col]);
         }
      }

      return res;
   }
}


const pacificAtlantic = new Solution().pacificAtlantic;
console.log((new Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]).sort().toString()) === ([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]).sort().toString()) === ([[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1]]).sort().toString()) === ([[0, 0]]).sort().toString())
