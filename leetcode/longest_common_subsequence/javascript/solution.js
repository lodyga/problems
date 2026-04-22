class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array, string
    *     A: top-down
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const ROWS = text1.length;
      const COLS = text2.length;
      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));

      const dfs = (index1, index2) => {
         if (index1 === ROWS || index2 === COLS) {
            return 0
         } else if (memo[index1][index2] !== -1) {
            return memo[index1][index2]
         }

         const res = Math.max(
            dfs(index1 + 1, index2),
            dfs(index1, index2 + 1),
            text1[index1] === text2[index2] ? 1 + dfs(index1 + 1, index2 + 1) : 0
         );

         memo[index1][index2] = res;
         return res
      }

      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array, string
    *     A: bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const ROWS = text1.length;
      const COLS = text2.length;
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            if (text1[row] === text2[col]) {
               cache[row][col] = 1 + cache[row + 1][col + 1]
            } else {
               cache[row][col] = Math.max(
                  cache[row + 1][col],
                  cache[row][col + 1]
               )
            }
         }
      }

      return cache[0][0]
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array, string
    *     A: bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const ROWS = text1.length;
      const COLS = text2.length;
      let nextCache = Array(COLS + 1).fill(0);

      for (let row = ROWS - 1; row > -1; row--) {
         const cache = Array(COLS + 1).fill(0);
         
         for (let col = COLS - 1; col > -1; col--) {
            if (text1[row] === text2[col]) {
               cache[col] = 1 + nextCache[col + 1]
            } else {
               cache[col] = Math.max(
                  nextCache[col],
                  cache[col + 1]
               )
            }
         }

         nextCache = cache;
      }
      return nextCache[0]
   };
}


const longestCommonSubsequence = new Solution().longestCommonSubsequence;
console.log(new Solution().longestCommonSubsequence('abcde', 'ace') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'abc') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'def') === 0)
console.log(new Solution().longestCommonSubsequence('bsbininm', 'jmjkbkjkv') === 1)
console.log(new Solution().longestCommonSubsequence('pmjghexybyrgzczy', 'hafcdqbgncrcbihkd') === 4)
