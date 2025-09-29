class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * monotonically increasing stack
    * @param {number[]} prices
    * @return {number[]}
    */
   finalPrices(prices) {
      const stack = [];
      const discountPrices = [];

      for (const price of prices.reverse()) {
         while (stack && price < stack[stack.length - 1]) 
            stack.pop();

         discountPrices.push(price - (stack.length ? stack[stack.length - 1] : 0));
         stack.push(price);
      }
      return discountPrices.reverse()
   };
}
const finalPrices = new Solution().finalPrices;


console.log(new Solution().finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])
console.log(new Solution().finalPrices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
console.log(new Solution().finalPrices([10, 1, 1, 6]), [9, 0, 1, 6])
console.log(new Solution().finalPrices([5, 4, 3, 2, 1]), [1, 1, 1, 1, 1])