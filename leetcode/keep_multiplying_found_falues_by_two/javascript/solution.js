class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} nums
    * @param {number[]} original
    * @return {nums, original}
    */
   findFinalValue(nums, original) {
      const numSet = new Set(nums);
      while (numSet.has(original))
         original *= 2;
      return original
   };
}


const findFinalValue = new Solution().findFinalValue;
console.log(new Solution().findFinalValue([5, 3, 6, 1, 12], 3) === 24)
console.log(new Solution().findFinalValue([2, 7, 9], 4) === 4)
