class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n3)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number} m
    * @param {number} n
    * @param {number} maxMove
    * @param {number} startRow
    * @param {number} startColumn
    * @return {number}
    */
   findPaths(m, n, maxMove, startRow, startColumn) {
      const MOD = 10 ** 9 + 7;
      const ROWS = m;
      const COLS = n;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const memo = Array.from({ length: ROWS }, () =>
         Array.from({ length: COLS }, () =>
            Array(maxMove).fill(-1)));

      const dfs = (row, col, moves) => {
         if (
            row === -1 || row === ROWS ||
            col === -1 || col === COLS
         ) {
            return 1
         } else if (moves === maxMove) {
            return 0
         } else if (memo[row][col][moves] !== -1) {
            return memo[row][col][moves]
         }

         let res = 0
         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            res = (res + dfs(r, c, moves + 1)) % MOD
         }

         memo[row][col][moves] = res
         return res
      }

      return dfs(startRow, startColumn, 0)
   };

   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n3)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} m
    * @param {number} n
    * @param {number} maxMove
    * @param {number} startRow
    * @param {number} startColumn
    * @return {number}
    */
   findPaths(m, n, maxMove, startRow, startColumn) {
      const MOD = 10 ** 9 + 7;
      const ROWS = m;
      const COLS = n;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const cache = Array.from({ length: ROWS }, () =>
         Array.from({ length: COLS }, () =>
            Array(maxMove + 1).fill(0)));

      for (let move = maxMove - 1; move > -1; move--) {
         for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
               for (const [dr, dc] of DIRECTIONS) {
                  const [r, c] = [dr + row, dc + col];

                  if (
                     r === -1 || r === ROWS ||
                     c === -1 || c === COLS
                  ) {
                     cache[row][col][move]++
                  } else {
                     cache[row][col][move] = (
                        cache[row][col][move] + cache[r][c][move + 1]) % MOD
                  }
               }
            }
         }
      }

      return cache[startRow][startColumn][0]
   };

   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} m
    * @param {number} n
    * @param {number} maxMove
    * @param {number} startRow
    * @param {number} startColumn
    * @return {number}
    */
   findPaths(m, n, maxMove, startRow, startColumn) {
      const MOD = 10 ** 9 + 7;
      const ROWS = m;
      const COLS = n;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let nextCache = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

      for (let _ = maxMove - 1; _ > -1; _--) {
         const cache = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

         for (let row = 0; row < ROWS; row++) {
            for (let col = 0; col < COLS; col++) {
               for (const [dr, dc] of DIRECTIONS) {
                  const [r, c] = [dr + row, dc + col];

                  if (
                     r === -1 || r === ROWS ||
                     c === -1 || c === COLS
                  ) {
                     cache[row][col]++
                  } else {
                     cache[row][col] += nextCache[r][c]
                     // cache[row][col] = (
                     //    cache[row][col] + nextCache[r][c]) % MOD
                  }
               }
               cache[row][col] %= MOD;
            }
         }
         nextCache = cache;
      }

      return nextCache[startRow][startColumn]
   };
}



const findPaths = new Solution().findPaths;
console.log(new Solution().findPaths(2, 2, 0, 0, 0) === 0)
console.log(new Solution().findPaths(2, 2, 1, 0, 0) === 2)
console.log(new Solution().findPaths(2, 2, 2, 0, 0) === 6)
console.log(new Solution().findPaths(1, 3, 3, 0, 1) === 12)
console.log(new Solution().findPaths(8, 7, 16, 1, 5) === 102984580)
