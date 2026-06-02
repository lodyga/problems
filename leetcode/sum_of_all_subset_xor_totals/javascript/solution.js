class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: backtracking
    * @param {number[]} nums
    * @return {number}
    */
   subsetXORSum(nums) {
      const backtrack = (idx, xor) => {
         if (idx === nums.length) {
            return xor;
         }

         const num = nums[idx];
         const take = backtrack(idx + 1, xor ^ num);
         const skip = backtrack(idx + 1, xor);
         return take + skip;
      }
      
      return backtrack(0, 0);
   }
}


class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: backtracking
    * @param {number[]} nums
    * @return {number}
    */
   subsetXORSum(nums) {
      let res = 0;

      const backtrack = (idx, xor) => {
         if (idx === nums.length) {
            res += xor;
            return;
         }

         const num = nums[idx];
         backtrack(idx + 1, xor ^ num);
         backtrack(idx + 1, xor);
      }
      
      backtrack(0, 0);
      return res;
   }
}


const subsetXORSum = new Solution().subsetXORSum;
console.log(new Solution().subsetXORSum([1, 3]) === 6)
console.log(new Solution().subsetXORSum([5, 1, 6]) === 28)
console.log(new Solution().subsetXORSum([3, 4, 5, 6, 7, 8]) === 480)
