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

      const dfs = (index) => {
         // index: current string length
         if (index > high) {
            return 0
         } else if (memo[index] !== -1) {
            // elif index in memo:
            return memo[index]
         }

         let res = index >= low ? 1 : 0;
         res += dfs(index + zero);
         res += dfs(index + one);
         memo[index] = res;
         return res % MOD
      }
      return dfs(0)
   };

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
      const cache = Array(high + 1);
      cache[0] = 1;

      for (let index = 1; index <= high; index++) {
         let val = index >= zero ? cache[index - zero] : 0;
         val += index >= one ? cache[index - one] : 0;
         cache[index] = val % MOD;
      }

      let counter = 0;
      for (let index = low; index <= high; index++) {
         counter += cache[index];
      }

      return counter % MOD
   };
}


const countGoodStrings = new Solution().countGoodStrings;
console.log(new Solution().countGoodStrings(1, 1, 1, 1) === 2)
console.log(new Solution().countGoodStrings(2, 2, 1, 1) === 4)
console.log(new Solution().countGoodStrings(1, 2, 1, 1) === 6)
console.log(new Solution().countGoodStrings(1, 3, 1, 1) === 14)
console.log(new Solution().countGoodStrings(3, 3, 1, 1) === 8)
console.log(new Solution().countGoodStrings(2, 3, 1, 2) === 5)
console.log(new Solution().countGoodStrings(200, 200, 10, 1) === 764262396)
console.log(new Solution().countGoodStrings(1, 100000, 1, 1) === 215447031)
