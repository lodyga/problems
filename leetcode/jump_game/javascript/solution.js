class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {boolean}
    */
   canJump(nums) {
      let step = 0;

      for (let idx = 0; idx < nums.length - 1; idx++) {
         const num = nums[idx];
         step = Math.max(step - 1, nums[idx]);

         if (step === 0) {
            return false;
         }
      }

      return true;
   }
}


class Solution {
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
      const memo = Array(nums.length).fill(-1);
      memo[memo.length - 1] = 1;

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx];
         }

         memo[idx] = 0;
         const step = Math.min(idx + nums[idx], nums.length - 1)

         for (let jdx = idx + 1; jdx < step + 1; jdx++) {
            if (dfs(jdx)) {
               memo[idx] = 1;
               break;
            }
         }

         return memo[idx];
      }

      return Boolean(dfs(0));
   }
}


class Solution {
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

      for (let idx = nums.length - 2; idx > -1; idx--) {
         const step = Math.min(idx + nums[idx], nums.length - 1);
         
         for (let jdx = idx + 1; jdx < step + 1; jdx++) {
            if (cache[jdx]) {
               cache[idx] = true;
               break;
            }
         }
      }

      return cache[0];
   }
}


const canJump = new Solution().canJump;
console.log(new Solution().canJump([2, 3, 1, 1, 4]) === true)
console.log(new Solution().canJump([3, 2, 1, 0, 4]) === false)
console.log(new Solution().canJump([0]) === true)
console.log(new Solution().canJump([2, 0, 0]) === true)
console.log(new Solution().canJump([0, 2, 3]) === false)
console.log(new Solution().canJump([1, 0, 1, 0]) === false)
console.log(new Solution().canJump([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]) === false)
