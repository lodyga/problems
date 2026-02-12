class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number} n
    * @return {}
    */
   numTrees(n) {
      const memo = Array(Math.max(n + 1, 2)).fill(-1);
      memo[0] = 1;
      memo[1] = 1;

      const dfs = (n) => {
         if (memo[n] !== -1)
            return memo[n]

         let res = 0;
         for (let index = 0; index < n; index++) {
            const left = dfs(index);
            const right = dfs(n - index - 1);
            res += left * right;
         }

         memo[n] = res;
         return res
      }
      return dfs(n)
   };
}


const numTrees = new Solution().numTrees;
console.log(new Solution().numTrees(1) === 1)
console.log(new Solution().numTrees(2) === 2)
console.log(new Solution().numTrees(3) === 5)
console.log(new Solution().numTrees(19) === 1767263190)
