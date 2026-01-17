class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} nums
    * @return {boolean}
    */
   canJump(nums) {
      let step = 1;

      for (let index = 0; index < nums.length - 1; index++) {
         step = Math.max(step - 1, nums[index]);

         if (step === 0) {
            return false
         }
      }
      return Boolean(step)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} nums
    * @return {boolean}
    */
   canJump(nums) {
      const memo = Array(nums.length);
      memo[memo.length - 1] = true;

      const dfs = (index) => {
         if (memo[index] !== undefined)
            return memo[index]

         memo[index] = false;
         const maxJump = Math.min(index + nums[index], nums.length - 1)
         for (let i2 = maxJump; i2 > index; i2--) {
            if (dfs(i2)) {
               memo[index] = true;
               break
            }
         }
         return memo[index]
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums
    * @return {boolean}
    */
   canJump(nums) {
      const cache = Array(nums.length).fill(false);
      cache[cache.length - 1] = true;

      for (let index = nums.length - 2; index > -1; index--) {
         const maxJump = Math.min(index + nums[index], nums.length - 1);
         for (let i2 = maxJump; i2 > index; i2--) {
            if (cache[i2]) {
               cache[index] = true
               break
            }
         }
      }
      return cache[0]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {boolean}
    */
   canJump(nums) {
      let maxJump = 1;
      for (let index = 0; index < nums.length - 1; index++) {
         maxJump = Math.max(maxJump - 1, nums[index]);
         if (maxJump === 0)
            return false
      }
      return true
   };
}


const canJump = new Solution().canJump;
console.log(new Solution().canJump([2, 3, 1, 1, 4]) === true)
console.log(new Solution().canJump([3, 2, 1, 0, 4]) === false)
console.log(new Solution().canJump([0]) === true)
console.log(new Solution().canJump([2, 0, 0]) === true)
console.log(new Solution().canJump([0, 2, 3]) === false)
console.log(new Solution().canJump([1, 0, 1, 0]) === false)
console.log(new Solution().canJump([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]) === false)
