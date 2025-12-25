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
      const combinations = [];

      const backtrack = (index) => {
         if (index == n) {
            if (combination.length === k)
               combinations.push(combination.slice());
            return
         }
         combination.push(index + 1);
         backtrack(index + 1);
         combination.pop();
         backtrack(index + 1);
      }
      backtrack(0)
      return combinations
   };

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
      const combinations = [];

      const backtrack = (index) => {
         if (combination.length === k) {
            combinations.push(combination.slice());
            return
         }
         for (let num = index; num < n + 1; num++) {
            combination.push(num);
            backtrack(num + 1);
            combination.pop();
         }
      }
      backtrack(1)
      return combinations
   };
}


const combine = new Solution().combine;
console.log(JSON.stringify(new Solution().combine(1, 1)) === JSON.stringify([[1]]))
console.log(JSON.stringify(new Solution().combine(2, 2)) === JSON.stringify([[1, 2]]))
console.log(JSON.stringify(new Solution().combine(4, 2)) === JSON.stringify([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
