class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy (Kadane)
    * @param {number[]} nums
    * @return {number}
    */
   maxProduct(nums) {
      let maxProd = nums[0];
      let minTotal = 1;
      let maxTotal = 1;

      for (const num of nums) {
         const triplet = [minTotal * num, maxTotal * num, num];
         minTotal = Math.min(...triplet);
         maxTotal = Math.max(...triplet);
         maxProd = Math.max(maxProd, maxTotal);
      }
      return maxProd
   };
}


const maxProduct = new Solution().maxProduct;
console.log(new Solution().maxProduct([-2]) === -2)
console.log(new Solution().maxProduct([-4, -3]) === 12)
console.log(new Solution().maxProduct([2, 3, -2, 4]) === 6)
console.log(new Solution().maxProduct([-2, 0, -1]) === 0)
console.log(new Solution().maxProduct([-2, -3, 7]) === 42)
console.log(new Solution().maxProduct([2, -5, -2, -4, 3]) === 24)
console.log(new Solution().maxProduct([0]) === 0)
console.log(new Solution().maxProduct([-2, 0]) === 0)
console.log(new Solution().maxProduct([0, 2]) === 2)
