import { Queue } from "@datastructures-js/queue";


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
   closedIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const dfs = (row, col) => {
         if (
            row === -1 || row === ROWS ||
            col === -1 || col === COLS
         ) {
            return false
         } else if (visited[row][col]) {
            return true
         } else if (grid[row][col]) {
            visited[row][col] = true;
            return true
         }

         visited[row][col] = true;
         let isClosed = true;

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            isClosed &= dfs(r, c);
         }
         return isClosed
      };

      let res = 0;
      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (
               grid[row][col] == 0 &&
               !visited[row][col]
            )
               res += dfs(row, col);
      return res
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} grid
    * @return {number}
    */
   closedIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

      const bfs = (row, col) => {
         const queue = new Queue([[row, col]]);
         // queue.enqueue([row, col]);
         visited[row][col] = true;
         let isClosed = true;

         while (queue.size()) {
            const [row, col] = queue.dequeue();

            for (const [dr, dc] of DIRECTIONS) {
               const[r, c] = [row + dr, col + dc];

               if (
                  r === -1 || r === ROWS ||
                  c === -1 || c === COLS
               ) {
                  isClosed = false;
                  continue
               }
               else if (visited[r][c] || grid[r][c]) {
                  continue
               }
               queue.enqueue([r, c]);
               grid[r][c] = true;
            }
         }
         return isClosed
      };

      let res = 0;
      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (
               grid[row][col] == 0 &&
               !visited[row][col]
            )
               res += bfs(row, col);
      return res
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
