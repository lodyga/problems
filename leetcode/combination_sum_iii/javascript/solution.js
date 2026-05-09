class Solution {
   /**
    * Time complexity: O(1)
    *     O(2^9)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {number} k
    * @param {number} target
    * @return {number[][]}
    */
   combinationSum3(k, target) {
      const combination = [];
      const res = [];

      const dfs = (digit, total) => {
         if (combination.length === k) {
            if (total === target) {
               res.push(combination.slice());
            }
            return
         } else if (
            digit === 10 ||
            total >= target
         ) return

         combination.push(digit);
         dfs(digit + 1, total + digit);
         combination.pop();
         dfs(digit + 1, total);
      }
      
      dfs(1, 0);
      return res
   }
}


const combinationSum3 = new Solution().combinationSum3;
console.log(JSON.stringify(new Solution().combinationSum3(2, 4)) === JSON.stringify([[1, 3]]))
console.log(JSON.stringify(new Solution().combinationSum3(3, 7)) === JSON.stringify([[1, 2, 4]]))
console.log(JSON.stringify(new Solution().combinationSum3(3, 9)) === JSON.stringify([[1, 2, 6], [1, 3, 5], [2, 3, 4]]))
console.log(JSON.stringify(new Solution().combinationSum3(4, 1)) === JSON.stringify([]))
