class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array(memoization):
    *     A: top-down
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const rows = text1.length;
      const cols = text2.length;
      const memo = Array.from({ length: rows }, () => Array(cols).fill(-1));

      const dfs = (index1, index2) => {
         if (index1 === rows || index2 === cols) {
            return 0
         } else if (memo[index1][index2] !== -1) {
            return memo[index1][index2]
         }

         const take = text1[index1] === text2[index2] ? 1 + dfs(index1 + 1, index2 + 1) : 0;
         const skip1 = dfs(index1 + 1, index2);
         const skip2 = dfs(index1, index2 + 1);

         memo[index1][index2] = Math.max(take, skip1, skip2);
         return memo[index1][index2]
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array(tabulation):
    *     A: bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const rows = text1.length;
      const cols = text2.length;
      const cache = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));

      for (let row = rows - 1; row > -1; row--) {
         for (let col = cols - 1; col > -1; col--) {
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
    *     DS: array(tabulation):
    *     A: bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const rows = text1.length;
      const cols = text2.length;
      const cache = Array(cols + 1).fill(0);
      const nextCache = cache.slice();

      for (let row = rows - 1; row > -1; row--) {
         for (let col = cols - 1; col > -1; col--) {
            if (text1[row] === text2[col]) {
               cache[col] = 1 + nextCache[col + 1]
            } else {
               cache[col] = Math.max(
                  nextCache[col],
                  cache[col + 1]
               )
            }
         }
         cache.forEach((value, index) => nextCache[index] = value);
      }
      return cache[0]
   };
}


const longestCommonSubsequence = new Solution().longestCommonSubsequence;
console.log(new Solution().longestCommonSubsequence('abcde', 'ace') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'abc') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'def') === 0)
console.log(new Solution().longestCommonSubsequence('bsbininm', 'jmjkbkjkv') === 1)
console.log(new Solution().longestCommonSubsequence('pmjghexybyrgzczy', 'hafcdqbgncrcbihkd') === 4)
