class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @return {boolean}
    */
   isMonotonic(nums) {
      let prev = nums[0];
      let isIncreasing = true;
      let isDecreasing = true;

      for (const num of nums) {
         if (prev > num)
            isDecreasing = false;
         if (prev < num)
            isIncreasing = false;
         prev = num;
      }
      return isIncreasing || isDecreasing
   };
}


const isMonotonic = new Solution().isMonotonic;
console.log(new Solution().isMonotonic([1, 2, 2, 3]) === true)
console.log(new Solution().isMonotonic([6, 5, 4, 4]) === true)
console.log(new Solution().isMonotonic([1, 3, 2]) === false)
