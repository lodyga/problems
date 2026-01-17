class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration, negative marking
    * @param {number[]} nums
    * @return {number}
    */
   firstMissingPositive(nums) {
      const N = nums.length;
      
      for (let index = 0; index < N; index++) {
         const num = nums[index];
         if (num <= 0) {
            nums[index] = N + 1;
         }
      }
      for (let index = 0; index < N; index++) {
         const num = Math.abs(nums[index]);
         if (num <= N) {
            nums[num - 1] = -Math.abs(nums[num - 1]);
         }
      }
      for (let index = 0; index < N; index++) {
         const num = nums[index];
         if (num > 0) {
            return index + 1
         }
      }
      return N + 1
   };
}


const firstMissingPositive = new Solution().firstMissingPositive;
console.log(new Solution().firstMissingPositive([1, 2, 0]) === 3)
console.log(new Solution().firstMissingPositive([3, 4, -1, 1]) === 2)
console.log(new Solution().firstMissingPositive([7, 8, 9, 11, 12]) === 1)
