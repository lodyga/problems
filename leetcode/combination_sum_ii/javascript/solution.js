class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    *     n: candidates length
    * Tags: backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum2(candidates, target) {
      candidates.sort((a, b) => a - b);
      const combination = [];
      const combinationList = [];

      function dfs(index) {
         const combinationSum = combination.reduce((sum, value) => sum + value, 0);
         if (combinationSum === target) {
            combinationList.push(combination.slice());
            return
         } else if (
            combinationSum > target ||
            index === candidates.length
         ) return

         combination.push(candidates[index]);
         dfs(index + 1);
         combination.pop();
         while (
            index + 1 < candidates.length &&
            candidates[index] === candidates[index + 1]
         ) index++;
         dfs(index + 1);
      }
      dfs(0);
      return combinationList
   };
}


class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    *     n: candidates length
    * Tags: iterative dfs with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum2(candidates, target) {
      candidates.sort((a, b) => a - b);
      const combination = [];
      const combinationList = [];

      function dfs(start) {
         const combinationSum = combination.reduce((sum, value) => sum + value, 0);
         if (combinationSum === target) {
            combinationList.push(combination.slice());
            return
         } else if (combinationSum > target) 
            return

         for (let index = start; index < candidates.length; index++) {
            if (index > start && candidates[index] === candidates[index - 1])
               continue
            combination.push(candidates[index]);
            dfs(index + 1);
            combination.pop();
         }

      }
      dfs(0);
      return combinationList
   };
}


console.log(new Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
console.log(new Solution().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
console.log(new Solution().combinationSum2([6], 6), [[6]])
console.log(new Solution().combinationSum2([2, 2, 2], 2), [[2]])