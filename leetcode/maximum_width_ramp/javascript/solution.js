class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing stack
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   maxWidthRamp(nums) {
      const stack = [];
      let res = 0;

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         if (stack.length === 0 || nums[stack[stack.length - 1]] > num) {
            stack.push(index);
         }
      }

      for (let index = nums.length - 1; index > -1; index--) {
         const num = nums[index];

         while (stack.length && nums[stack[stack.length - 1]] <= num) {
            res = Math.max(res, index - stack[stack.length - 1]);
            stack.pop();
         }
      }

      return res
   };
}


const maxWidthRamp = new Solution().maxWidthRamp;
console.log(new Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]) === 4)
console.log(new Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) === 7)
console.log(new Solution().maxWidthRamp([8, 6, 0, 8, 2, 7, 7]) === 5)
