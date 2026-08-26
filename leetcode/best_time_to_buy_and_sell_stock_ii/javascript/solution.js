class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: greedy
    * @param {number[]} prices
    * @return {number}
    */
   maxProfit(prices) {
      let res = 0;
      let prevPrice = prices[0];

      for (const price of prices) {
         if (price > prevPrice) {
            res += price - prevPrice;
         }

         prevPrice = price;
      }

      return res;
   }
}


const maxProfit = new Solution().maxProfit;
console.log(new Solution().maxProfit([7, 1]) === 0)
console.log(new Solution().maxProfit([1, 7]) === 6)
console.log(new Solution().maxProfit([7, 1, 5, 3, 6, 4]) === 7)
console.log(new Solution().maxProfit([1, 2, 3, 4, 5]) === 4)
console.log(new Solution().maxProfit([7, 6, 4, 3, 1]) === 0)
