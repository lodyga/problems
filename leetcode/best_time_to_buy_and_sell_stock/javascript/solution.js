class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      if (prices.length === 0)
         return 0
      let maxProf = 0;
      let minPrice = prices[0];

      for (const price of prices) {
         if (price < minPrice) {
            minPrice = price;
         } else {
            const profit = price - minPrice;
            if (profit > maxProf) {
               maxProf = profit;
            }
         }
      }
      return maxProf
   };
}


console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]), 0)
console.log(new Solution().maxProfit([2, 4, 1]), 2)
console.log(new Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]), 2)
console.log(new Solution().maxProfit([1, 2]), 1)