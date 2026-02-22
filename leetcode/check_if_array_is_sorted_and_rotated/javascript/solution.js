class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     iteration
    * @param {number[]} nums
    * @return {boolean}
    */
   check(nums) {
      let pivot = -1;

      for (let index = 0; index < nums.length; index++) {
         if (nums[index] > nums[(index + 1) % nums.length]) {
            pivot++;

            if (pivot) {
               return false
            }
         }
      }
      return true
   };
}


const check = new Solution().check;
console.log(new Solution().check([3, 4, 5, 1, 2]) === true);
console.log(new Solution().check([2, 1, 3, 4]) === false);
console.log(new Solution().check([1, 2, 3]) === true);
console.log(new Solution().check([6, 10, 6]) === true)
