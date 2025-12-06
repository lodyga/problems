class Solution {
   /**
    * Time complexity: O(n2^n)
    *     n: candidates length
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: DFS with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum2(candidates, target) {
      candidates.sort((a, b) => a - b);
      const combination = [];
      const combinationList = [];

      const backtrack = (index, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (
            total > target ||
            index === candidates.length
         ) return

         const candidate = candidates[index];
         combination.push(candidate);
         backtrack(index + 1, total + candidate);
         combination.pop();
         while (
            index + 1 < candidates.length &&
            candidate === candidates[index + 1]
         ) index++;

         backtrack(index + 1, total);
      }
      backtrack(0, 0);
      return combinationList
   };

   /**
    * Time complexity: O(n2^n)
    *     n: candidates length
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: DFS with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum2(candidates, target) {
      candidates.sort((a, b) => a - b);
      const combination = [];
      const combinationList = [];

      const backtrack = (start, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (total > target)
            return

         for (let index = start; index < candidates.length; index++) {
            const candidate = candidates[index]
            if (
               index > start &&
               candidate === candidates[index - 1]
            ) continue

            combination.push(candidate);
            backtrack(index + 1, total + candidate);
            combination.pop();
         }

      }
      backtrack(0, 0);
      return combinationList
   };
}


const combinationSum2 = new Solution().combinationSum2;
console.log(new Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
console.log(new Solution().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
console.log(new Solution().combinationSum2([6], 6), [[6]])
console.log(new Solution().combinationSum2([2, 2, 2], 2), [[2]])
