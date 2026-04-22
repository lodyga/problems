class Solution {
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
      const res = Array(nums.length).fill(0);
      res[0] = 1;

      for (let idx = 1; idx < nums.length; idx++) {
         const num = nums[idx - 1];
         res[idx] = res[idx - 1] * num;
      }

      let suffix = 1;

      for (let idx = nums.length - 1; idx > -1; idx--) {
         res[idx] *= suffix;
         res[idx] += 0;
         suffix *= nums[idx];
      }

      return res
   };
}


const productExceptSelf = new Solution().productExceptSelf;
console.log(new Solution().productExceptSelf([2, 3, 4, 5]).toString() === [60, 40, 30, 24].toString())
console.log(new Solution().productExceptSelf([1, 2, 3, 4]).toString() === [24, 12, 8, 6].toString())
console.log(new Solution().productExceptSelf([-1, 1, 0, -3, 3]).toString() === [0, 0, 9, 0, 0].toString())
