class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number} low
    * @param {number} high
    * @param {number} zero
    * @param {number} one
    * @return {number}
    */
   countGoodStrings(low, high, zero, one) {
      const MOD = 10 ** 9 + 7;
      const memo = Array(high + Math.max(zero, one)).fill(-1);

      const dfs = (idx) => {
         if (idx > high) {
            return 0;
         } else if (memo[idx] !== -1) {
            return memo[idx];
         }

         let res = idx >= low ? 1 : 0;
         res += dfs(idx + zero);
         res += dfs(idx + one);
         memo[idx] = res;
         return res % MOD
      }

      return dfs(0);
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} low
    * @param {number} high
    * @param {number} zero
    * @param {number} one
    * @return {number}
    */
   countGoodStrings(low, high, zero, one) {
      const MOD = 10 ** 9 + 7;
      const cache = Array(high + 1).fill(0);
      cache[high] = 1;
      let res = 0;

      for (let idx = high - 1; idx > - 1; idx--) {
         if (idx + zero <= high) {
            cache[idx] += cache[idx + zero];
         }

         if (idx + one <= high) {
            cache[idx] += cache[idx + one];
         }

         cache[idx] = cache[idx] % MOD;
      }

      for (let idx = 0; idx < high - low + 1; idx++) {
         res += cache[idx];
      }

      return res % MOD;
   }
}


const countGoodStrings = new Solution().countGoodStrings;
console.log(new Solution().countGoodStrings(2, 3, 1, 2) === 5)
console.log(new Solution().countGoodStrings(1, 1, 1, 1) === 2)
console.log(new Solution().countGoodStrings(2, 2, 1, 1) === 4)
console.log(new Solution().countGoodStrings(1, 2, 1, 1) === 6)
console.log(new Solution().countGoodStrings(1, 3, 1, 1) === 14)
console.log(new Solution().countGoodStrings(3, 3, 1, 1) === 8)
console.log(new Solution().countGoodStrings(200, 200, 10, 1) === 764262396)
console.log(new Solution().countGoodStrings(1, 100000, 1, 1) === 215447031)
