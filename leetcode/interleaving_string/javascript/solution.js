class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), string
    *     A: top-down
    * @param {string} s1
    * @param {string} s2
    * @param {string} s3
    * @return {boolean}
    */
   isInterleave(s1, s2, s3) {
      if (s1.length + s2.length !== s3.length) {
         return false
      }
      // {(index1, index2): can_fold}
      // can_fold: {true: Yes, False: No, null: donno}
      const memo = Array.from({ length: s1.length }, () => Array(s2.length).fill(null));

      const dfs = (index1, index2) => {
         const index3 = index1 + index2;

         if (index1 === s1.length) {
            return s3.slice(index3,) === s2.slice(index2,)
         } else if (index2 == s2.length) {
            return s3.slice(index3,) === s1.slice(index1,)
            e
         } else if (memo[index1][index2] !== null) {
            return memo[index1][index2]
         }

         const letter1 = s1[index1];
         const letter2 = s2[index2];
         const letter3 = s3[index3];

         if (letter1 === letter3 && dfs(index1 + 1, index2)) {
            memo[index1][index2] = true;
            return true
         } else if (letter2 === letter3 && dfs(index1, index2 + 1)) {
            memo[index1][index2] = true;
            return true
         }

         memo[index1][index2] = false;
         return false
      };
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix), string
    *     A: bottom-up
    * @param {string} s1
    * @param {string} s2
    * @param {string} s3
    * @return {boolean}
    */
   isInterleave(s1, s2, s3) {
      if (s1.length + s2.length !== s3.length) {
         return false
      }
      const ROWS = s1.length;
      const COLS = s2.length;
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(false));
      cache[ROWS][COLS] = true;

      for (let row = ROWS; row > -1; row--) {
         for (let col = COLS; col > -1; col--) {
            const index = row + col;

            if (
               row < ROWS &&
               s1[row] == s3[index] &&
               cache[row + 1][col]
            )
               cache[row][col] = true;
            else if (
               col < COLS &&
               s2[col] == s3[index] &&
               cache[row][col + 1]
            )
               cache[row][col] = true;
         }
      }
      return cache[0][0]
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix), string
    *     A: bottom-up
    * @param {string} s1
    * @param {string} s2
    * @param {string} s3
    * @return {boolean}
    */
   isInterleave(s1, s2, s3) {
      if (s1.length + s2.length !== s3.length) {
         return false
      }
      const ROWS = s1.length;
      const COLS = s2.length;
      let nextCache = Array(COLS + 1).fill(false);
      nextCache[COLS] = true;

      for (let row = ROWS; row > -1; row--) {
         const cache = Array(COLS + 1).fill(false);
         if (row === ROWS)
                cache[COLS] = true;

         for (let col = COLS; col > -1; col--) {
            const index = row + col;

            if (
               row < ROWS &&
               s1[row] == s3[index] &&
               nextCache[col]
            )
               cache[col] = true;
            else if (
               col < COLS &&
               s2[col] == s3[index] &&
               cache[col + 1]
            )
               cache[col] = true;
         }
         nextCache = cache;
      }
      return nextCache[0]
   };
}


const isInterleave = new Solution().isInterleave;
console.log(new Solution().isInterleave('aa', 'bb', 'aabb') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc') === false)
console.log(new Solution().isInterleave('', '', '') === true)
console.log(new Solution().isInterleave('cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc', 'abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb', 'abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb') === true)
