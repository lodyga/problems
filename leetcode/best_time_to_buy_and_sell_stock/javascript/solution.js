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
      let res = 0;
      let minPrice = prices[0];

      for (const price of prices) {
         if (price > minPrice) {
            res = Math.max(res, price - minPrice);
         } else {
            minPrice = price;
         }
      }

      return res
   };
}


const maxProfit = new Solution().maxProfit;
console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]) === 5)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]) === 0)
console.log(new Solution().maxProfit([2, 4, 1]) === 2)
console.log(new Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) === 2)
console.log(new Solution().maxProfit([1, 2]) === 1)
