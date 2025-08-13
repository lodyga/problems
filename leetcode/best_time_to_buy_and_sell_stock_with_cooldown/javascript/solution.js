class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      const memo = new Map();

      const dfs = (index, buying) => {
         if (index >= prices.length) {
            return 0
         } else if (memo.has(`${index},${buying}`)) {
            return memo.get(`${index},${buying}`)
         } else if (buying) {
            memo.set(`${index},${buying}`, 
               Math.max(
                  dfs(index + 1, true),
                  -prices[index] + dfs(index + 1, false)
               )
            )
         } else {
            memo.set(`${index},${buying}`, 
               Math.max(
                  dfs(index + 1, false),
                  prices[index] + dfs(index + 2, true)
               )
            )
         }
         return memo.get(`${index},${buying}`)
      }
      return dfs(0, true)
   };
}
const maxProfit = new Solution().maxProfit;


console.log(new Solution().maxProfit([1, 2, 3, 0, 2]) === 3)
console.log(new Solution().maxProfit([1]) === 0)
console.log(new Solution().maxProfit([2, 1, 4]) === 3)