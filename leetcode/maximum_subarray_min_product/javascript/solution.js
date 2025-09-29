class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[]} numbers
    * @return {number}
    */
   maxSumMinProduct(numbers) {
      
   };
}


console.log(new Solution().maxSumMinProduct([1]), 1)  // [1] * 1
console.log(new Solution().maxSumMinProduct([1, 2]), 4)  // [2] * 2
console.log(new Solution().maxSumMinProduct([1, 2, 3]), 10)  // [2, 3] * 2
console.log(new Solution().maxSumMinProduct([1, 2, 3, 2]), 14)  // [2, 3, 2] * 2
console.log(new Solution().maxSumMinProduct([2, 3, 3, 1, 2]), 18)  // [3, 3] * 3
console.log(new Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]), 60)  // [5, 6, 4] * 4