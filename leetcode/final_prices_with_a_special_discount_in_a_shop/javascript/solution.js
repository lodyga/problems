class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    * @param {number[]} prices
    * @return {number[]}
    */
   finalPrices(prices) {
      const discountPrices = prices.slice();
      const stack = [];

      for (let index = 0; index < prices.length; index++) {
         const price = prices[index];
         while (stack.length && stack[stack.length - 1][0] >= price) {
            const [, prevIndex] = stack.pop();
            discountPrices[prevIndex] -= price;
         }

         stack.push([price, index]);
      }
      return discountPrices
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: monotonic increasing stack
    * @param {number[]} prices
    * @return {number[]}
    */
   finalPrices(prices) {
      const stack = [];

      for (let index = 0; index < prices.length; index++) {
         const price = prices[index];
         while (stack.length && prices[stack[stack.length - 1]] >= price) {
            const prevIndex = stack.pop();
            prices[prevIndex] -= prices[index];
         }

         stack.push(index);
      }
      return prices
   };
}


const finalPrices = new Solution().finalPrices;
console.log(new Solution().finalPrices([8, 4, 6, 2, 3]).toString() === [4, 2, 4, 2, 3].toString())
console.log(new Solution().finalPrices([1, 2, 3, 4, 5]).toString() === [1, 2, 3, 4, 5].toString())
console.log(new Solution().finalPrices([5, 4, 3, 2, 1]).toString() === [1, 1, 1, 1, 1].toString())
console.log(new Solution().finalPrices([10, 1, 1, 6]).toString() === [9, 0, 1, 6].toString())
