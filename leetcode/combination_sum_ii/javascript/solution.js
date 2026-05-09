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

      const backtrack = (idx, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (
            total > target ||
            idx === candidates.length
         ) return

         const candidate = candidates[idx];
         combination.push(candidate);
         backtrack(idx + 1, total + candidate);
         combination.pop();

         while (
            idx + 1 < candidates.length &&
            candidate === candidates[idx + 1]
         ) idx++;

         backtrack(idx + 1, total);
      }
      backtrack(0, 0);
      return combinationList
   }
}


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

      const backtrack = (start, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (total > target) return

         for (let idx = start; idx < candidates.length; idx++) {
            const candidate = candidates[idx]
            if (
               idx > start &&
               candidate === candidates[idx - 1]
            ) continue

            combination.push(candidate);
            backtrack(idx + 1, total + candidate);
            combination.pop();
         }

      }
      backtrack(0, 0);
      return combinationList
   }
}


const combinationSum2 = new Solution().combinationSum2;
console.log(new Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8).sort().toString() === [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]].sort().toString())
console.log(new Solution().combinationSum2([2, 5, 2, 1, 2], 5).sort().toString() === [[1, 2, 2], [5]].sort().toString())
console.log(new Solution().combinationSum2([6], 6).sort().toString() === [[6]].sort().toString())
console.log(new Solution().combinationSum2([2, 2, 2], 2).sort().toString() === [[2]].sort().toString())
