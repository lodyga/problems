class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: greedy
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      let maxProfit = 0;
      let minPrice = prices[0];

      for (const price of prices) {
         minPrice = Math.min(minPrice, price);
         const profit = price - minPrice;
         maxProfit = Math.max(maxProfit, profit);
      }
      return maxProfit
   };
}


const maxProfit = new Solution().maxProfit;
console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]) == 0)
console.log(new Solution().maxProfit([2, 4, 1]) == 2)
console.log(new Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2)
console.log(new Solution().maxProfit([1, 2]) == 1)
