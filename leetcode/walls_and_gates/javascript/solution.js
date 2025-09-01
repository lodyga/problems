class Solution {
   /**
    * Time complexity: O(n4)
    *     may vistit the same land more than once
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, graph, matrix
    * @param {number[][]} grid
    * @return {number[][]}
    */
   islandsAndTreasure(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col] === 0) {
               dfs(row, col, 0)
            }
         }
      }
      return grid

      function dfs(row , col, distance) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] < distance ||
            (distance && grid[row][col] === 0)
         ) return

         grid[row][col] = Math.min(grid[row][col], distance);
         DIRECTIONS.map(([r, c]) => dfs(row + r, col + c, distance + 1))
      }
   };
}


import { Queue } from '@datastructures-js/queue';

class Solution {
   /**
    * Time complexity: O(n4)
    *     may vistit the same land more than once
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, iteration, queue, matrix, graph
    * @param {number[][]} grid
    * @return {number[][]}
    */
   islandsAndTreasure(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col] === 0) {
               dfs(row, col, 0)
            }
         }
      }
      return grid

      function dfs(row , col, distance) {
         const queue = new Queue([[row, col, distance]]);


         while (!queue.isEmpty()) {
            const [row, col, distance] = queue.pop();
            grid[row][col] = Math.min(grid[row][col], distance);

            for (const [r, c] of DIRECTIONS) {
               if (
                  0 <= row + r &&
                  0 <= col + c &&
                  row + r < rows &&
                  col + c < cols &&
                  grid[row + r][col + c] > distance
               ) {
                  queue.push([row + r, col + c, distance + 1]);
               }
            }
         }
      }
   };
}


console.log(new Solution().islandsAndTreasure([[0, -1], [Infinity, Infinity]]), [[0, -1], [1, 2]])
console.log(new Solution().islandsAndTreasure([[Infinity, Infinity, Infinity], [Infinity, -1, Infinity], [0, Infinity, Infinity]]), [[2, 3, 4], [1, -1, 3], [0, 1, 2]])
console.log(new Solution().islandsAndTreasure([[Infinity, -1, 0, Infinity], [Infinity, Infinity, Infinity, -1], [Infinity, -1, Infinity, -1], [0, -1, Infinity, Infinity]]), [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])