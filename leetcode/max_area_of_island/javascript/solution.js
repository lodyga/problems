import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: bfs, iteration, queue, graph, matrix
    * @param {number[][]} grid
    * @return {number}
    */
   maxAreaOfIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      let maxArea = 0;

      const bfs = (row, col) => {
         visited[row][col] = true;
         let area = 1
         const queue = new Queue([[row, col]]);

         while (!queue.isEmpty()) {
            const [row, col] = queue.dequeue();

            for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
               if (
                  r === -1 ||
                  c === -1 ||
                  r === ROWS ||
                  c === COLS ||
                  grid[r][c] === 0 ||
                  visited[r][c]
               ) continue
               
               queue.enqueue([r, c]);
               visited[r][c] = true;
               area++;
            }
         }
         return area
      }

      for (let row = 0; row < ROWS; row++)
         for (let col = 0; col < COLS; col++)
            if (
               grid[row][col] &&
               !visited[row][col]
            )
               maxArea = Math.max(maxArea, bfs(row, col));

      return maxArea
   }
};


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, graph, matrix
    * @param {number[][]} grid
    * @return {number}
    */
   maxAreaOfIsland(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
      let maxArea = 0;

      const dfs = (row, col) => {
         if (
            row === -1 ||
            col === -1 ||
            row === ROWS ||
            col === COLS ||
            grid[row][col] === 0 ||
            visited[row][col]
         ) return 0

         visited[row][col] = true;

         let area = 1
         for (const [r, c] of DIRECTIONS.map(([r, c]) => [r + row, c + col])) {
            area += dfs(r, c)
         }
         return area
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            maxArea = Math.max(maxArea, dfs(row, col));
         }
      }

      return maxArea
   };
}


const maxAreaOfIsland = new Solution().maxAreaOfIsland;
console.log(new Solution().maxAreaOfIsland([[0]]) === 0)
console.log(new Solution().maxAreaOfIsland([[1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[0, 0], [0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 0], [0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]) === 3)
console.log(new Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) === 6)
console.log(new Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) === 0)