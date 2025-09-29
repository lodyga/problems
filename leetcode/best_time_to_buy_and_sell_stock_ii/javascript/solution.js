class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      if (prices.length === 1)
         return 0

      let profit = 0;

      for (let index = 1; index < prices.length; index++) {
         if (prices[index - 1] < prices[index]) {
            profit += prices[index] - prices[index - 1];
         }
      }
      return profit
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoziation as hash map
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      const memo = new Map();

      const dfs = (index, canBuy) => {
         if (index === prices.length) {
            return 0
         } else if (memo.has(`${index}.${canBuy}`)) {
            return memo.get(`${index}.${canBuy}`)
         }
         let profit = 0;
         if (canBuy) {
            profit = Math.max(
               -prices[index] + dfs(index + 1, false),
               dfs(index + 1, true)
            );
         } else {
            profit = Math.max(
               prices[index] + dfs(index + 1, true),
               dfs(index + 1, false)
            );
         }

         memo.set(`${index}.${canBuy}`, profit);
         return profit
      }
      return dfs(0, true)
   };
}
const maxProfit = new Solution().maxProfit;


console.log(new Solution().maxProfit([7, 1]) === 0)
console.log(new Solution().maxProfit([1, 7]) === 6)
console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]) === 7)
console.log(new Solution().maxProfit([1, 2, 3, 4, 5]) === 4)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]) === 0)