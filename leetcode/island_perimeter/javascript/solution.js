import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array (matrix)
    *     A: iteration
    * @param {number[][]} grid
    * @return {number}
    */
   islandPerimeter(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let res = 0

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col]) {
               for (const [dr, dc] of DIRECTIONS) {
                  const [r, c] = [row + dr, col + dc];

                  if (
                     r === -1
                     || c === -1
                     || r === ROWS
                     || c === COLS
                     || grid[r][c] === 0
                  ) {
                     res++;
                  }
               }
            }
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: dfs, recursion
    * @param {number[][]} grid
    * @return {number}
    */
   islandPerimeter(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const dfs = (row, col) => {
         if (
            row === -1
            || row === ROWS
            || col === -1
            || col === COLS
            || grid[row][col] === 0
         ) {
            return 1
         }
         else if (visited[row][col]) {
            return 0
         }

         visited[row][col] = true;

         let res = 0;
         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            res += dfs(r, c)
         }

         return res;
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col]) {
               return dfs(row, col)
            }
         }
      }

      return 0;
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} grid
    * @return {number}
    */
   islandPerimeter(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const bfs = (row, col) => {
         let res = 0;
         const queue = new Queue([[row, col]]);
         visited[row][col] = true;

         while (queue.size()) {
            const [row, col] = queue.pop();

            for (const [dr, dc] of DIRECTIONS) {
               const [r, c] = [row + dr, col + dc];

               if (
                  r === -1
                  || c === -1
                  || r === ROWS
                  || c === COLS
                  || grid[r][c] === 0
               )
                  res++;

               else if (grid[r][c] === 1 && !visited[r][c]) {
                  queue.push([r, c]);
                  visited[r][c] = true;
               }
            }
         }

         return res;
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if (grid[row][col]) {
               return bfs(row, col)
            }
         }
      }

      return 0;
   }
}


const islandPerimeter = new Solution().islandPerimeter;
console.log(new Solution().islandPerimeter([[0]]) === 0)
console.log(new Solution().islandPerimeter([[1]]) === 4)
console.log(new Solution().islandPerimeter([[1, 0]]) === 4)
console.log(new Solution().islandPerimeter([[1, 1], [1, 1]]) === 8)
console.log(new Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) === 16)
