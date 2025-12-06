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
      const combinationList = [];

      backtrack = (index, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (
            total > target ||
            index === candidates.length
         ) return

         const candidate = candidates[index];
         combination.push(candidate);
         backtrack(index, total + candidate);
         combination.pop();
         backtrack(index + 1, total);
      }
      backtrack(0, 0);
      return combinationList
   };

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
      const combinationList = [];

      const backtrack = (index, total) => {
         if (total === target) {
            combinationList.push(combination.slice());
            return
         } else if (total > target)
            return

         for (let i2 = index; i2 < candidates.length; i2++) {
            const candidate = candidates[i2];
            combination.push(candidate);
            backtrack(i2, total + candidate);
            combination.pop();
         }
      }
      backtrack(0, 0);
      return combinationList
   };
}


const combinationSum = new Solution().combinationSum;
console.log(new Solution().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
console.log(new Solution().combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
console.log(new Solution().combinationSum([2], 1), [])
