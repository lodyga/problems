class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, matrix, graph
    * @param {number[][]} grid
    * @return {number}
    */
   closedIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      const dfs = (row, col) => {
         if (
            row === -1 ||
            row === ROWS ||
            col === -1 ||
            col === COLS
         )
            return false
         else if (grid[row][col] == 1)
            return true

         grid[row][col] = 1;

         let isClosedIsland = true;
         for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
            if (dfs(r, c) === false)
               isClosedIsland = false;
         }
         return isClosedIsland
      };

      let counter = 0;
      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (grid[row][col] == 0)
               counter += dfs(row, col)
      return counter
   };
}


import { Queue } from "@datastructures-js/queue";
class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, queue, matrix, graph
    * @param {number[][]} grid
    * @return {number}
    */
   closedIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      const bfs = (row, col) => {
         const queue = new Queue();
         queue.enqueue([row, col]);
         let isClosedIsland = true;

         while (!queue.isEmpty()) {
            const [row, col] = queue.dequeue();
            grid[row][col] = 1;

            for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
               if (
                  r === -1 ||
                  r === ROWS ||
                  c === -1 ||
                  c === COLS
               ) isClosedIsland = false;
               else if (grid[r][c] == 0) {
                  queue.enqueue([r, c])
                  grid[r][c] = 1;
               }
            }
         }
         return isClosedIsland
      };

      let counter = 0;
      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (grid[row][col] == 0)
               counter += bfs(row, col)
      return counter
   };
}


const closedIsland = new Solution().closedIsland;
console.log(new Solution().closedIsland([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) === 1)
console.log(new Solution().closedIsland([[0, 1], [1, 1]]) === 0)
console.log(new Solution().closedIsland([[1, 1, 1], [0, 0, 1], [1, 1, 1]]) === 0)
console.log(new Solution().closedIsland([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) === 1)
console.log(new Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) === 2)
console.log(new Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) === 1)
console.log(new Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) === 2)
console.log(new Solution().closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) === 5)