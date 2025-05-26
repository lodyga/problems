class Solution {
   /**
    * Time complexity: O(1)
    *     O(2^9)
    * Auxiliary space complexity: O(1)
    * Tags: backtracking
    * @param {number} combination_length
    * @param {number} total
    * @return {number[][]}
    */
   combinationSum3(combination_length, total) {
      const combination = [];
      const combinationList = [];
      dfs(1);
      return combinationList

      function dfs(digit) {
         if (
            combination.length === combination_length &&
            combination.reduce((total, value) => total + value, 0) === total
         ) {
            combinationList.push(combination.slice())
            return
         } else if (
            digit === 10 ||
            combination.length > combination_length ||
            combination.reduce((total, value) => total + value, 0) > total
         ) return

         combination.push(digit);
         dfs(digit + 1);
         combination.pop();
         dfs(digit + 1);
      }
   };
}


console.log(new Solution().combinationSum3(3, 7), [[1, 2, 4]])
console.log(new Solution().combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
console.log(new Solution().combinationSum3(4, 1), [])