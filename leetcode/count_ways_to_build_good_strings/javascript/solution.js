class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number} low
    * @param {number} high
    * @param {number} zero
    * @param {number} one
    * @return {number}
    */
   countGoodStrings(low, high, zero, one) {
      const mod = 10 ** 9 + 7;
      const cache = new Map([[0, 1]]);

      for (let index = 1; index <= high; index++) {
         const value = (
            (cache.get(index - zero) ?? 0) +
            (cache.get(index - one) ?? 0)) % mod;
         cache.set(index, value);
      }

      let counter = 0;
      for (let index = low; index <= high; index++) {
         counter += cache.get(index);
      }

      return counter % mod
   };
}


console.log(new Solution().countGoodStrings(1, 1, 1, 1), 2)
console.log(new Solution().countGoodStrings(2, 2, 1, 1), 4)
console.log(new Solution().countGoodStrings(1, 2, 1, 1), 6)
console.log(new Solution().countGoodStrings(1, 3, 1, 1), 14)
console.log(new Solution().countGoodStrings(3, 3, 1, 1), 8)
console.log(new Solution().countGoodStrings(2, 3, 1, 2), 5)
console.log(new Solution().countGoodStrings(200, 200, 10, 1), 764262396)
console.log(new Solution().countGoodStrings(1, 100000, 1, 1), 215447031)