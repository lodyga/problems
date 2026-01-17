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
      const subsetList = [];

      const backtrack = (index) => {
         if (index === nums.length) {
            subsetList.push(subset.slice());
            return
         }
         subset.push(nums[index]);
         backtrack(index + 1);
         subset.pop();
         backtrack(index + 1);
      }

      backtrack(0);
      return subsetList
   };

   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * A: DFS with backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsets(nums) {
      const subset = [];
      const subsetList = [];

      function backtrack(start) {
         subsetList.push(subset.slice());
         for (let index = start; index < nums.length; index++) {
            subset.push(nums[index]);
            backtrack(index + 1);
            subset.pop();
         }
      }
      backtrack(0);
      return subsetList
   };
}


const subsets = new Solution().subsets;
console.log(new Solution().subsets([0]), [[], [0]])
console.log(new Solution().subsets([1, 2]), [[], [1], [2], [1, 2]])
console.log(new Solution().subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

console.log(JSON.stringify((new Solution().subsets([0])).sort()) === JSON.stringify(([[], [0]]).sort()))
console.log(JSON.stringify((new Solution().subsets([1, 2])).sort()) === JSON.stringify([[], [1], [2], [1, 2]].sort()))
console.log(JSON.stringify((new Solution().subsets([1, 2, 3])).sort()) === JSON.stringify([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].sort()))
