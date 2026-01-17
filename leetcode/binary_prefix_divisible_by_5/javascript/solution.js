class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} nums
    * @return {boolean[]}
    */
   prefixesDivBy5(nums) {
      let prefix = 0;
      const isDivisible = Array(nums.length).fill(false);
      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         prefix = (prefix << 1 + num) % 5;
         isDivisible[index] = prefix === 0;
      }
      return isDivisible
   };
}


const prefixesDivBy5 = new Solution().prefixesDivBy5;
console.log(new Solution().prefixesDivBy5([0, 1, 1]), [true, false, false])
console.log(new Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]), [true, false, false, false, true, false])
console.log(new Solution().prefixesDivBy5([1, 1, 1]), [false, false, false])
console.log(new Solution().prefixesDivBy5([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]), [false, false, true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, false, false, false, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, false, false, false])
