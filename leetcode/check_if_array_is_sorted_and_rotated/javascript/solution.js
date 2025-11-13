class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} nums
    * @return {boolean}
    */
   check(nums) {
      let isRotated = false;

      for (let index = 1; index < nums.length; index++) {
         if (nums[index - 1] <= nums[index])
            continue

         if (isRotated)
            return false
         else
            isRotated = true;
      }
      return (
         !isRotated ||
         nums[nums.length - 1] <= nums[0]
      )
   };
}


const check = new Solution().check;
console.log(new Solution().check([3, 4, 5, 1, 2]) === true);
console.log(new Solution().check([2, 1, 3, 4]) === false);
console.log(new Solution().check([1, 2, 3]) === true);
