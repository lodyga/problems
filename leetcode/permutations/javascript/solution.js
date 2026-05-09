class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   permute(nums) {
      const res = [];

      const backtrack = (start) => {
         if (start === nums.length) {
            res.push(nums.slice());
            return
         }
         for (let idx = start; idx < nums.length; idx++) {
            [nums[start], nums[idx]] = [nums[idx], nums[start]];
            backtrack(start + 1);
            [nums[start], nums[idx]] = [nums[idx], nums[start]];
         }
      }

      backtrack(0);
      return res
   }
}


const permute = new Solution().permute;
console.log(new Solution().permute([1, 2, 3]).sort().toString() === [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].sort().toString())
console.log(new Solution().permute([0, 1]).sort().toString() === [[0, 1], [1, 0]].sort().toString())
console.log(new Solution().permute([1]).sort().toString() === [[1]].sort().toString())
