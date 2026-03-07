import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: queue, array (matrix)
    *     A: multi-source BFS
    * @param {number} m
    * @param {number} n
    * @param {number[][]} guards
    * @param {number[][]} wals
    * @return {}
    */
   countUnguarded(m, n, guards, walls) {
      const ROWS = m;
      const COLS = n;
      const DIRECTIONS = new Map([[0, [-1, 0]], [1, [1, 0]], [2, [0, -1]], [3, [0, 1]]]);
      // 1: not visited/safe; 0: visited/not safe; -1: wall/guard
      const grid = Array.from({ length: ROWS }, () => Array(COLS).fill(1));
      const queue = new Queue();

      for (const [row, col] of walls) {
         grid[row][col] = -1;
      }

      for (const [row, col] of guards) {
         grid[row][col] = -1;

         for (let direction = 0; direction < 4; direction++) {
            queue.enqueue([row, col, direction]);
         }
      }

      // bfs
      while (queue.size()) {
         const [row, col, direction] = queue.dequeue();
         const [dr, dc] = DIRECTIONS.get(direction);
         const [r, c] = [row + dr, col + dc];

         if (
            r == -1 || r == ROWS ||
            c == -1 || c == COLS ||
            grid[r][c] == -1
         ) {
            continue
         }

         queue.enqueue([r, c, direction])
         grid[r][c] = 0;
      }

      let res = 0;

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            res += grid[row][col] === 1 ? 1 : 0;
         }
      }

      return res
   };
}


const countUnguarded = new Solution().countUnguarded;
console.log(new Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]) === 7)
console.log(new Solution().countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]) === 4)
console.log(new Solution().countUnguarded(2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]) === 1)
