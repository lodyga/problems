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
      const isWeaklyIncreasing = (nums) => {
         let prevNum = nums[0] - 1;

         for (const num of nums) {
            if (prevNum > num) {
               return false;
            }

            prevNum = num;
         }

         return true;
      }

      const isWeaklyDecreasing = (nums) => {
         let prevNum = nums[0] + 1;

         for (const num of nums) {
            if (prevNum < num) {
               return false;
            }

            prevNum = num;
         }

         return true;
      }

      return (
         isWeaklyIncreasing(nums)
         || isWeaklyDecreasing(nums)
      );
   }
}


const isMonotonic = new Solution().isMonotonic;
console.log(new Solution().isMonotonic([1, 2, 2, 3]) === true)
console.log(new Solution().isMonotonic([6, 5, 4, 4]) === true)
console.log(new Solution().isMonotonic([1, 3, 2]) === false)
