import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    *     n: heights length
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), hash set
    *     A: multi-source DFS
    * @param {number[][]} heights
    * @return {number[][]}
    */
   pacificAtlantic(heights) {
      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const toPacific = new Set();
      const toAtlantic = new Set();

      const dfs = (row, col, ocean, prevHeight) => {
         if (
            row == -1 ||
            col == -1 ||
            row == ROWS ||
            col == COLS ||
            heights[row][col] < prevHeight ||
            ocean.has(`${row},${col}`)
         ) return

         ocean.add(`${row},${col}`);

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            dfs(r, c, ocean, heights[row][col]);
         }
      }

      for (let row = 0; row < ROWS; row++) {
         dfs(row, 0, toPacific, heights[row][0]);
         dfs(row, COLS - 1, toAtlantic, heights[row][COLS - 1]);
      }

      for (let col = 0; col < COLS; col++) {
         dfs(0, col, toPacific, heights[0][col]);
         dfs(ROWS - 1, col, toAtlantic, heights[ROWS - 1][col])
      }

      const toOceanTiles = [];
      for (const coordinates of toPacific) {
         if (toAtlantic.has(coordinates))
            toOceanTiles.push(coordinates.split(',').map(Number))
      }
      return toOceanTiles
   };

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
      const ROWS = heights.length;
      const COLS = heights[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const toPacific = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      const toAtlantic = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const bfs = (oceanQueue, toOcean) => {
         while (oceanQueue.size()) {
            const [row, col] = oceanQueue.pop();
            toOcean[row][col] = true;

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];
               if (
                  r == -1 ||
                  c == -1 ||
                  r == ROWS ||
                  c == COLS ||
                  heights[r][c] < heights[row][col] ||
                  toOcean[r][c] === true
               ) continue

               oceanQueue.push([r, c]);
               toOcean[r][c] = true;
            }
         }
      }

      const pacificQueue = new Queue();
      const atlanticQueue = new Queue();
      for (let row = 0; row < ROWS; row++) {
         pacificQueue.push([row, 0])
         atlanticQueue.push([row, COLS - 1])
      }
      for (let col = 0; col < COLS; col++) {
         pacificQueue.push([0, col])
         atlanticQueue.push([ROWS - 1, col])
      }
      bfs(pacificQueue, toPacific);
      bfs(atlanticQueue, toAtlantic);

      const toOceanTiles = [];
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (toPacific[row][col] && toAtlantic[row][col])
               toOceanTiles.push([row, col]);
         }
      }
      return toOceanTiles
   };
}


const pacificAtlantic = new Solution().pacificAtlantic;
console.log((new Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]).sort().toString()) === ([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]).sort().toString()) === ([[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]).sort().toString())
console.log((new Solution().pacificAtlantic([[1]]).sort().toString()) === ([[0, 0]]).sort().toString())
