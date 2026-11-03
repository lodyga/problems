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

      const dfs = (idx1, idx2) => {
         const idx3 = idx1 + idx2;
         let res = false;

         if (idx1 === ROWS) {
            return s2.slice(idx2,) === s3.slice(idx3,);
         }
         else if (idx2 == COLS) {
            return s1.slice(idx1,) === s3.slice(idx3,);
         }
         else if (memo[idx1][idx2] !== -1) {
            return Boolean(memo[idx1][idx2]);
         }

         if (s1[idx1] === s3[idx3]) {
            res = dfs(idx1 + 1, idx2);
         }
         if (s2[idx2] === s3[idx3]) {
            const a = dfs(idx1, idx2 + 1);
            res ||= a;
         }

         memo[idx1][idx2] = Number(res);
         return res;
      };

      const ROWS = s1.length;
      const COLS = s2.length;

      if (ROWS + COLS !== s3.length) {
         return false;
      }

      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));
      return dfs(0, 0);
   }
}


class Solution {
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
      const ROWS = s1.length;
      const COLS = s2.length;

      if (ROWS + COLS !== s3.length) {
         return false;
      }

      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(false));
      cache[ROWS][COLS] = true;

      for (let row = ROWS; row > -1; row--) {
         for (let col = COLS; col > -1; col--) {
            const idx = row + col;

            if (
               row < ROWS
               && s1[row] === s3[idx]
               && cache[row + 1][col]
            ) {
               cache[row][col] = true;
            }
            else if (
               col < COLS
               && s2[col] === s3[idx]
               && cache[row][col + 1]
            ) {
               cache[row][col] = true;
            }
         }
      }

      return cache[0][0];
   }
}


class Solution {
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
      const ROWS = s1.length;
      const COLS = s2.length;

      if (ROWS + COLS !== s3.length) {
         return false;
      }

      let nextCache = Array(COLS + 1).fill(false);
      nextCache[COLS] = true;

      for (let row = ROWS; row > -1; row--) {
         const cache = Array(COLS + 1).fill(false);

         if (row === ROWS) {
            cache[COLS] = true;
         }

         for (let col = COLS; col > -1; col--) {
            const idx = row + col;

            if (
               row < ROWS
               && s1[row] === s3[idx]
               && nextCache[col]
            ) {
               cache[col] = true;
            }
            else if (
               col < COLS
               && s2[col] === s3[idx]
               && cache[col + 1]
            ) {
               cache[col] = true;
            }
         }

         nextCache = cache;
      }

      return nextCache[0];
   }
}


const isInterleave = new Solution().isInterleave;
console.log(new Solution().isInterleave('aa', 'bb', 'aabb') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc') === false)
console.log(new Solution().isInterleave('', '', '') === true)
console.log(new Solution().isInterleave('cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc', 'abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb', 'abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb') === true)
