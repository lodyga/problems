class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsets(nums) {
      const subset = [];
      const res = [];

      const backtrack = (idx) => {
         if (idx === nums.length) {
            res.push(subset.slice());
            return
         }

         subset.push(nums[idx]);
         backtrack(idx + 1);
         subset.pop();
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
    *     A: DFS with backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsets(nums) {
      const subset = [];
      const res = [];

      const backtrack = (start) => {
         res.push(subset.slice());

         for (let idx = start; idx < nums.length; idx++) {
            subset.push(nums[idx]);
            backtrack(idx + 1);
            subset.pop();
         }
      }

      backtrack(0);
      return res
   }
}


const subsets = new Solution().subsets;
// console.log(new Solution().subsets([0]), [[], [0]])
// console.log(new Solution().subsets([1, 2]), [[], [1], [2], [1, 2]])
// console.log(new Solution().subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
console.log(new Solution().subsets([0]).sort().toString() === [[], [0]].sort().toString())
console.log(new Solution().subsets([1, 2]).sort().toString() === [[], [1], [2], [1, 2]].sort().toString())
console.log(new Solution().subsets([1, 2, 3]).sort().toString() === [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].sort().toString())
