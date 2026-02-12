import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: dfs, recursion 
    * @param {string[][]} grid
    * @return {number}
    */
   numIslands(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const dfs = (row, col) => {
         if (
            row == -1 ||
            col == -1 ||
            row === ROWS ||
            col === COLS ||
            grid[row][col] === '0' ||
            visited[row][col]
         ) return 0

         visited[row][col] = true;
         DIRECTIONS.map(([r, c]) => dfs(row + r, col + c));
         return 1
      }

      let islandCounter = 0;
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            islandCounter += dfs(row, col)
         }
      }
      return islandCounter
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration 
    * @param {string[][]} grid
    * @return {number}
    */
   numIslands(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const bfs = (row, col) => {
         if (
            grid[row][col] == "0" ||
            visited[row][col]
         ) return 0

         const queue = new Queue([[row, col]]);
         visited[row][col] = true;

         while (queue.size()) {
            const [row, col] = queue.pop();

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r == -1 ||
                  c == -1 ||
                  r === ROWS ||
                  c === COLS ||
                  grid[r][c] === '0' ||
                  visited[r][c]
               ) continue

               queue.push([r, c]);
               visited[r][c] = true;
            }
         }
         return 1
      };

      let islandCounter = 0;
      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            islandCounter += bfs(row, col)
         }
      }
      return islandCounter
   };
}


const numIslands = new Solution().numIslands;
console.log(new Solution().numIslands([['0']]) === 0)
console.log(new Solution().numIslands([['1']]) === 1)
console.log(new Solution().numIslands([['0', '0'], ['0', '1']]) === 1)
console.log(new Solution().numIslands([['1', '0'], ['0', '1']]) === 2)
console.log(new Solution().numIslands([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]) === 3)
console.log(new Solution().numIslands([['1', '1', '0'], ['0', '1', '0'], ['0', '0', '1']]) === 2)
console.log(new Solution().numIslands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]) === 1)
console.log(new Solution().numIslands([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]) === 3)
