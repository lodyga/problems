class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: hash map
    *     A: math, iteration
    * @param {number[]} nums
    * @return {number}
    */
   tupleSameProduct(nums) {
      const prodCounter = new Map();
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         const numR = nums[right];
         
         for (let left = 0; left < right; left++) {
            const numL = nums[left];
            const prod = numL * numR;
            prodCounter.set(prod, (prodCounter.get(prod) || 0) + 1);
         }
      }

      for (const counter of prodCounter.values()) {
         // Arithmetic series.
         const total = Math.floor((1 + (counter - 1)) * (counter - 1) / 2);
         const tupleCount = total * 8;
         res += tupleCount;
      }

      return res
   };
}


const tupleSameProduct = new Solution().tupleSameProduct;
console.log(new Solution().tupleSameProduct([2, 3, 4, 6]) === 8)
console.log(new Solution().tupleSameProduct([1, 2, 4, 5, 10]) === 16)
console.log(new Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]) === 40)
console.log(new Solution().tupleSameProduct([10, 5, 15, 8, 6, 12, 20, 4]) === 72)
console.log(new Solution().tupleSameProduct([30, 28, 20, 6, 24, 3, 12, 14, 2, 1]) === 72)
