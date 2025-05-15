class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   maxProduct(numbers) {
      let maxProd = numbers[0];
      const cache = [1, 1];

      for (const number of numbers) {
         const triplet = [
            number,
            cache[0] * number,
            cache[1] * number
         ];
         cache[0] = Math.max(...triplet);
         cache[1] = Math.min(...triplet);
         maxProd = Math.max(maxProd, cache[0])
      }
      return maxProd
   };
}


console.log(new Solution().maxProduct([-4, -3]), 12)
console.log(new Solution().maxProduct([2, 3, -2, 4]), 6)
console.log(new Solution().maxProduct([-2]), -2)
console.log(new Solution().maxProduct([-4, -3]), 12)
console.log(new Solution().maxProduct([-2, 0, -1]), 0)
console.log(new Solution().maxProduct([-2, -3, 7]), 42)
console.log(new Solution().maxProduct([2, -5, -2, -4, 3]), 24)
console.log(new Solution().maxProduct([-2]), -2)
console.log(new Solution().maxProduct([0]), 0)
console.log(new Solution().maxProduct([-2, 0]), 0)
console.log(new Solution().maxProduct([0, 2]), 2)