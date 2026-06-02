class Solution2 {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * @param {number} n
    * @param {number} k
    * @return {number[][]}
    */
   combine(n, k) {
      const combination = [];
      const res = [];

      const backtrack = (idx) => {
         if (combination.length === k) {
            res.push(combination.slice());
            return;
         } else if (idx === n + 1) {
            return;
         }

         combination.push(idx);
         backtrack(idx + 1);
         combination.pop();
         backtrack(idx + 1);
      }

      backtrack(1);
      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: backtracking
    * @param {number} n
    * @param {number} k
    * @return {number[][]}
    */
   combine(n, k) {
      const combination = [];
      const res = [];

      const backtrack = (idx) => {
         if (combination.length === k) {
            res.push(combination.slice());
            return;
         }

         for (let num = idx; num < n + 1; num++) {
            combination.push(num);
            backtrack(num + 1);
            combination.pop();
         }
      }

      backtrack(1);
      return res;
   }
}


const combine = new Solution().combine;
console.log(JSON.stringify(new Solution().combine(1, 1)) === JSON.stringify([[1]]))
console.log(JSON.stringify(new Solution().combine(2, 2)) === JSON.stringify([[1, 2]]))
console.log(JSON.stringify(new Solution().combine(4, 2)) === JSON.stringify([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
