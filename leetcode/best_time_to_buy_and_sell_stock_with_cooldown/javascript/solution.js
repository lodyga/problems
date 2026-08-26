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
      /**
       * @param {number} idx 
       * @param {number} canBuy 
       * @returns {number}
       */
      const dfs = (idx, canBuy) => {
         if (memo[idx][canBuy] !== -1) {
            return memo[idx][canBuy];
         }

         const price = prices[idx];
         let buy = 0;
         let sell = 0;
         const skip = dfs(idx + 1, canBuy);

         if (canBuy) {
            buy = -price + dfs(idx + 1, 0);
         }
         else {
            sell = price + dfs(idx + 2, 1);
         }

         const res = Math.max(skip, buy, sell);
         memo[idx][canBuy] = res;
         return res;
      };

      const N = prices.length;
      const memo = Array.from({ length: N + 2 }, () => Array(2).fill(-1));
      memo[N] = [0, 0];
      memo[N + 1] = [0, 0];

      return dfs(0, 1);
   }
}


class Solution {
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
      const N = prices.length;
      const cache = Array.from({ length: N + 2 }, () => Array(2).fill(0));
      cache[N] = [0, 0];
      cache[N + 1] = [0, 0];

      for (let idx = N - 1; idx > -1; idx--) {
         const price = prices[idx];
         cache[idx][1] = Math.max(  // can buy
            cache[idx + 1][1],  // skip
            -price + cache[idx + 1][0]  // buy
         );
         cache[idx][0] = Math.max(  // can sell
            cache[idx + 1][0],  // skip
            price + cache[idx + 2][1]  // sell
         );
      }

      return cache[0][1];
   }
}


class Solution {
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

      for (let idx = prices.length - 1; idx > -1; idx--) {
         const price = prices[idx];
         const buyCache = Math.max(  // can buy
            cache[0][1],  // skip
            -price + cache[0][0]  // buy
         )
         const sellCache = Math.max(  // can sell
            cache[0][0],  // skip
            price + cache[1][1]  // sell
         )
         cache[1][0] = cache[0][0];
         cache[1][1] = cache[0][1];
         cache[0][0] = sellCache;
         cache[0][1] = buyCache;
      }

      return cache[0][1];
   }
}


const maxProfit = new Solution().maxProfit;
console.log(new Solution().maxProfit([1, 2, 3, 0, 2]) === 3)
console.log(new Solution().maxProfit([1]) === 0)
console.log(new Solution().maxProfit([2, 1, 4]) === 3)
