class Solution {
   /**
    * Time complexity: O(1)
    *     O(2^9)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: list
    *     A: DFS with backtracking
    * @param {number} k
    * @param {number} total
    * @return {number[][]}
    */
   combinationSum3(k, total) {
      const combination = [];
      const combinationList = [];

      const dfs = (digit) => {
         if (
            combination.length === k &&
            combination.reduce((total, num) => total + num, 0) === total
         ) {
            combinationList.push(combination.slice())
            return
         } else if (
            digit === 10 ||
            combination.length == k ||
            combination.reduce((total, num) => total + num, 0) >= total
         ) return

         combination.push(digit);
         dfs(digit + 1);
         combination.pop();
         dfs(digit + 1);
      }
      dfs(1);
      return combinationList
   };
}


const combinationSum3 = new Solution().combinationSum3;
console.log(JSON.stringify(new Solution().combinationSum3(2, 4)) === JSON.stringify([[1, 3]]))
console.log(JSON.stringify(new Solution().combinationSum3(3, 7)) === JSON.stringify([[1, 2, 4]]))
console.log(JSON.stringify(new Solution().combinationSum3(3, 9)) === JSON.stringify([[1, 2, 6], [1, 3, 5], [2, 3, 4]]))
console.log(JSON.stringify(new Solution().combinationSum3(4, 1)) === JSON.stringify([]))
