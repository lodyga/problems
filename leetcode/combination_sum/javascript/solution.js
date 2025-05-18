class Solution {
   /**
    * Time complexity: O(n2^(t/m))
    *     t: target
    *     m: min from candidates
    * Auxiliary space complexity: O(n)
    *     n: candidates length
    * Tags: backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum(candidates, target) {
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
         dfs(index);
         combination.pop();
         dfs(index + 1);
      }
      dfs(0);
      return combinationList
   };
}


class Solution {
   /**
    * Time complexity: O(n2^(t/m))
    *     t: target
    *     m: min from candidates
    * Auxiliary space complexity: O(n)
    *     n: candidates length
    * Tags: iterative dfs with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum(candidates, target) {
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
            combination.push(candidates[index]);
            dfs(index);
            combination.pop();
         }
      }
      dfs(0);
      return combinationList
   };
}


console.log(new Solution().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
console.log(new Solution().combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
console.log(new Solution().combinationSum([2], 1), [])