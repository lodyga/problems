class Solution {
   /**
    * Time complexity: O(k2)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: array (matrix)
    *     A: multi-source DFS, topological sort with cycle detection
    *     Model: graph
    * @param {number} k
    * @param {number[][]} rowConds
    * @param {number[][]} colConds
    * @return {number[][]}
    */
   buildMatrix(k, rowConds, colConds) {

      const dfs = (col, sorted, visited, prevs) => {
         if (visited[col] !== -1)
            return Boolean(visited[col])

         visited[col] = 1;

         for (const prevCol of prevs[col])
            if (dfs(prevCol, sorted, visited, prevs))
               return true

         sorted.push(col);
         visited[col] = 0;
         return false;
      };

      const ROWS = k;
      const COLS = k;

      const prevCols = Array.from({ length: COLS }, () => []);
      for (const [prevVertex, vertex] of colConds)
         prevCols[vertex - 1].push(prevVertex - 1);

      const prevRows = Array.from({ length: ROWS }, () => []);
      for (const [prevVertex, vertex] of rowConds)
         prevRows[vertex - 1].push(prevVertex - 1);

      const sortedCols = [];
      // -1: not visited, 0: visited, 1: visiting/current path
      const visitedCols = Array(COLS).fill(-1);

      for (let col = 0; col < COLS; col++)
         if (dfs(col, sortedCols, visitedCols, prevCols))
            return []

      const sortedRows = [];
      // -1: not visited, 0: visited, 1: visiting/current path
      const visitedRows = Array(ROWS).fill(-1);

      for (let row = 0; row < ROWS; row++)
         if (dfs(row, sortedRows, visitedRows, prevRows))
            return []

      const coords = new Map(Array.from({length: k}, (_, v) => [v, []]));

      for (let row = 0; row < ROWS; row++) {
         const val = sortedRows[row];
         coords.get(val).push(row);
      }
      for (let col = 0; col < COLS; col++) {
         const val = sortedCols[col];
         coords.get(val).push(col);
      }

      const res = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
      for (let val = 0; val < k; val++) {
         const [y, x] = coords.get(val);
         res[y][x] = val + 1;
      }

      return res
   };
}


const buildMatrix = new Solution().buildMatrix;
console.log(new Solution().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]).toString() === [[0, 0, 1], [3, 0, 0], [0, 2, 0]].toString())
console.log(new Solution().buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]).toString() === [].toString())
