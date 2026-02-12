class Solution {
   /**
    * Time complexity: O(n3)
    *     O(n*t*k)
    *     n: dice count
    *     k: die side count
    *     t: target
    * Auxiliary space complexity: O(n2)
    *     O(n*t)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number} n
    * @param {number} k
    * @param {number} target
    * @return {number}
    */
   numRollsToTarget(n, k, target) {
      const MOD = 1e9 + 7;
      const memo = new Map();

      const dfs = (index, total) => {
         if (index === n) {
            return total == target ? 1 : 0
         } else if (total > target) {
            return 0
         } else if (memo.has(`${index},${total}`)) {
            return memo.get(`${index},${total}`)
         }

         let res = 0;

         for (let side = 1; side < k + 1; side++) {
            res += dfs(index + 1, total + side);
         }

         res %= MOD;
         memo.set(`${index},${total}`, res);
         return res
      }

      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n3)
    *     O(n*t*k)
    *     n: dice count
    *     k: die side count
    *     t: target
    * Auxiliary space complexity: O(n2)
    *     O(n*t)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number} n
    * @param {number} k
    * @param {number} target
    * @return {number}
    */
   numRollsToTarget(n, k, target) {
      const MOD = 1e9 + 7;
      const memo = Array.from({ length: n }, () => Array(target + 1).fill(-1));

      const dfs = (index, total) => {
         if (index === n) {
            return total == target ? 1 : 0
         } else if (total > target) {
            return 0
         } else if (memo[index][total] !== -1) {
            return memo[index][total]
         }

         let res = 0;

         for (let side = 1; side < k + 1; side++) {
            res += dfs(index + 1, total + side);
         }

         res %= MOD
         memo[index][total] = res;
         return res
      }

      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n3)
    *     O(n*t*k)
    *     n: dice count
    *     k: die side count
    *     t: target
    * Auxiliary space complexity: O(n2)
    *     O(n*t)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} n
    * @param {number} k
    * @param {number} target
    * @return {number}
    */
   numRollsToTarget(n, k, target) {
      const MOD = 1e9 + 7;
      const cache = Array.from({ length: n + 1 }, () => Array(target + 1).fill(0));
      cache[cache.length - 1][cache[0].length - 1] = 1;

      for (let index = n - 1; index > -1; index--) {
         for (let side = 1; side < k + 1; side++) {
            for (let total = 0; total < target + 1 - side; total++) {
               cache[index][total] += cache[index + 1][total + side];
               cache[index][total] %= MOD;
            }
         }
      }

      return cache[0][0]
   };
}


const numRollsToTarget = new Solution().numRollsToTarget;
console.log(new Solution().numRollsToTarget(1, 6, 3) === 1)
console.log(new Solution().numRollsToTarget(2, 6, 7) === 6)
console.log(new Solution().numRollsToTarget(3, 6, 9) === 25)
console.log(new Solution().numRollsToTarget(30, 30, 500) === 222616187)
