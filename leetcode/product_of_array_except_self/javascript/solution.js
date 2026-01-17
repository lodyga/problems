class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: prefix sum
    * @param {number[]} nums
    * @return {number[]}
    */
   productExceptSelf(nums) {
      const postfix = Array(nums.length).fill(0);
      postfix[postfix.length - 1] = 1;

      for (let index = nums.length - 1; index > 0; index--) {
         const num = nums[index];
         postfix[index - 1] = postfix[index] * num;
      }

      const product = Array(nums.length).fill(1);
      let prefix = 1;

      for (let index = 0; index < nums.length; index++) {
         product[index] = prefix * postfix[index];
         const num = nums[index];
         prefix *= num;
      }

      return product
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: prefix sum
    * @param {number[]} nums
    * @return {number[]}
    */
   productExceptSelf(nums) {
      const postfix = Array(nums.length).fill(0);
      postfix[postfix.length - 1] = 1;

      for (let index = nums.length - 1; index > 0; index--) {
         const num = nums[index];
         postfix[index - 1] = postfix[index] * num;
      }

      let prefix = 1;

      for (let index = 0; index < nums.length; index++) {
         postfix[index] *= prefix;
         const num = nums[index];
         prefix *= num;
      }

      return postfix
   };
}


const productExceptSelf = new Solution().productExceptSelf;
console.log(new Solution().productExceptSelf([2, 3, 4, 5]), [60, 40, 30, 24])
console.log(new Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
console.log(new Solution().productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
