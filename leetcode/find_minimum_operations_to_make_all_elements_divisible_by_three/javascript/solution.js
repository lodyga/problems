class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   minimumOperations(nums) {
      return nums
         .map(val => val % 3)
         .filter(val => val)
         .length
   };
}


const minimumOperations = new Solution().minimumOperations;
console.log(new Solution().minimumOperations([1, 2, 3, 4]) === 3)
console.log(new Solution().minimumOperations([3, 6, 9]) === 0)
