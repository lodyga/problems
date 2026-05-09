class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * Largest → Smallest
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsetsWithDup(nums) {
      const subset = [];
      const res = [];
      nums.sort((a, b) => a - b);

      const backtrack = (idx) => {
         if (idx === nums.length) {
            res.push(subset.slice());
            return
         }

         subset.push(nums[idx]);
         backtrack(idx + 1);
         subset.pop();

         while (
            idx + 1 < nums.length &&
            nums[idx] === nums[idx + 1]
         ) idx++;

         backtrack(idx + 1);
      }
      backtrack(0);
      return res
   }
}


class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * Largest → Smallest
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsetsWithDup(nums) {
      const subset = [];
      const res = [];
      nums.sort((a, b) => a - b);

      const backtrack = (start) => {
         res.push(subset.slice());

         for (let idx = start; idx < nums.length; idx++) {
            if (
               idx > start &&
               nums[idx] === nums[idx - 1]
            ) continue
            
            subset.push(nums[idx]);
            backtrack(idx + 1);
            subset.pop();
         }
      }

      backtrack(0)
      return res
   }
}


const subsetsWithDup = new Solution().subsetsWithDup;
console.log(new Solution().subsetsWithDup([0]).sort().toString() === [[], [0]].sort().toString())
console.log(new Solution().subsetsWithDup([5, 5]).sort().toString() === [[], [5], [5, 5]].sort().toString())
console.log(new Solution().subsetsWithDup([1, 2, 2]).sort().toString() === [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]].sort().toString())
console.log(new Solution().subsetsWithDup([4, 4, 4, 1, 4]).sort().toString() === [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]].sort().toString())
