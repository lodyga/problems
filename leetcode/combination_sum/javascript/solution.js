class Solution {
   /**
    * Time complexity: O(n2^(t/m))
    *     n: candidates length
    *     t: target
    *     m: min from candidates
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum(candidates, target) {
      const combination = [];
      const res = [];

      const backtrack = (idx, total) => {
         if (total === target) {
            res.push(combination.slice());
            return
         } else if (
            total > target ||
            idx === candidates.length
         ) return

         const candidate = candidates[idx];
         combination.push(candidate);
         backtrack(idx, total + candidate);
         combination.pop();
         backtrack(idx + 1, total);
      }

      backtrack(0, 0);
      return res
   }
}


class Solution {
   /**
    * Time complexity: O(n2^(t/m))
    *     n: candidates length
    *     t: target
    *     m: min from candidates
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {number[]} candidates
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum(candidates, target) {
      const combination = [];
      const res = [];

      const backtrack = (start, total) => {
         if (total === target) {
            res.push(combination.slice());
            return
         } else if (total > target)
            return

         for (let idx = start; idx < candidates.length; idx++) {
            const candidate = candidates[idx];
            combination.push(candidate);
            backtrack(idx, total + candidate);
            combination.pop();
         }
      }
      backtrack(0, 0);
      return res
   }
}


const combinationSum = new Solution().combinationSum;
console.log(new Solution().combinationSum([2, 3, 6, 7], 7).sort().toString() === [[2, 2, 3], [7]].sort().toString())
console.log(new Solution().combinationSum([2, 3, 5], 8).sort().toString() === [[2, 2, 2, 2], [2, 3, 3], [3, 5]].sort().toString())
console.log(new Solution().combinationSum([2], 1).sort().toString() === [].sort().toString())
