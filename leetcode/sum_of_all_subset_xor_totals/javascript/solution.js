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

      const backtrack = (index, xor) => {
         if (index === nums.length) {
            res += xor;
            return
         }
         backtrack(index + 1, xor ^ nums[index])
         backtrack(index + 1, xor)
      }
      backtrack(0, 0)
      return res
   };

   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: dfs, recursion
    * @param {number[]} nums
    * @return {number}
    */
   subsetXORSum(nums) {
      const dfs = (index, xor) => {
         if (index === nums.length) {
            return xor
         }
         const take = dfs(index + 1, xor ^ nums[index])
         const skip = dfs(index + 1, xor)
         return take + skip
      }
      return dfs(0, 0)
   };
}


const subsetXORSum = new Solution().subsetXORSum;
console.log(new Solution().subsetXORSum([1, 3]) === 6)
console.log(new Solution().subsetXORSum([5, 1, 6]) === 28)
console.log(new Solution().subsetXORSum([3, 4, 5, 6, 7, 8]) === 480)
