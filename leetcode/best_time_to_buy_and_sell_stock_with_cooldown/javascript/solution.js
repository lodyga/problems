class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      const memo = Array.from({ length: prices.length + 2 }, () => Array(2).fill(-1));
      memo[memo.length - 1] = [0, 0];
      memo[memo.length - 2] = [0, 0];

      /**
       * canBuy: 0: false, 1: true
       * @param {number} index 
       * @param {number} canBuy 
       * @returns {number}
       */
      const dfs = (index, canBuy) => {
         if (memo[index][canBuy] !== -1) {
            return memo[index][canBuy]
         }
         const price = prices[index];
         let [buy, sell] = [0, 0];
         const skip = dfs(index + 1, canBuy);
         if (canBuy) {
            buy = -price + dfs(index + 1, 0);
         } else {
            sell = price + dfs(index + 2, 1);
         }
         const res = Math.max(skip, buy, sell);
         memo[index][canBuy] = res;
         return res
      }
      return dfs(0, 1)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      const cache = Array.from({ length: prices.length + 2 }, () => Array(2).fill(-1));
      cache[cache.length - 1] = [0, 0];
      cache[cache.length - 2] = [0, 0];

      for (let index = prices.length - 1; index > -1; index--) {
         const price = prices[index];
         // can buy
         cache[index][1] = Math.max(
            cache[index + 1][1], // skip
            -price + cache[index + 1][0] // buy
         )
         // can sell
         cache[index][0] = Math.max(
            cache[index + 1][0], // skip
            price + cache[index + 2][1] // sell
         )
      }
      return cache[0][1]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      const cache = [[0, 0], [0, 0]]

      for (let index = prices.length - 1; index > -1; index--) {
         const price = prices[index];
         // can buy
         const buyCache = Math.max(
            cache[0][1], // skip
            -price + cache[0][0] // buy
         )
         // can sell
         const sellCache = Math.max(
            cache[0][0], // skip
            price + cache[1][1] // sell
         )
         cache[1][0] = cache[0][0];
         cache[1][1] = cache[0][1];
         cache[0][0] = sellCache;
         cache[0][1] = buyCache;
      }
      return cache[0][1]
   };
}


const maxProfit = new Solution().maxProfit;
console.log(new Solution().maxProfit([1, 2, 3, 0, 2]) === 3)
console.log(new Solution().maxProfit([1]) === 0)
console.log(new Solution().maxProfit([2, 1, 4]) === 3)
