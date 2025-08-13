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


console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]) === 7)
console.log(new Solution().maxProfit([1, 2, 3, 4, 5]) === 4)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]) === 0)