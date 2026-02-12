class Solution {
   /**
    * Time complexity: O((V + E) * q)
    *     q: query length
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: DFS
    *     Model: graph
    * @param {string[][]} equations
    * @param {number[]} values
    * @param {string[][]} queries
    * @return {number[]}
    */
   calcEquation = (equations, values, queries) => {
      const adjs = new Map();
      for (let index = 0; index < values.length; index++) {
         const [u, v] = equations[index];
         const val = values[index];
         if (!adjs.has(u))
            adjs.set(u, []);
         if (!adjs.has(v))
            adjs.set(v, []);
         adjs.get(u).push([v, val]);
         adjs.get(v).push([u, 1 / val]);
      }

      const visited = new Set();

      const dfs = (src, dst, visited) => {
         if (
            !adjs.has(src) ||
            visited.has(src)
         ) {
            return -1
         } else if (src === dst) {
            return 1
         }

         visited.add(src);

         for (const [adj_dst, adj_val] of adjs.get(src)) {
            const res = dfs(adj_dst, dst, visited);
            if (res !== -1) {
               return res * adj_val
            }
         }

         return -1
      };

      return queries.map(([src, dst]) => dfs(src, dst, new Set()))
   };
}


const calcEquation = new Solution().calcEquation;
console.log(new Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]).toString() === [6.00000, 0.50000, -1.00000, 1.00000, -1.00000].toString())
console.log(new Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]).toString() === [3.75000, 0.40000, 5.00000, 0.20000].toString())
console.log(new Solution().calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]).toString() === [0.50000, 2.00000, -1.00000, -1.00000].toString())
