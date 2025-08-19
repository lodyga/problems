class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down witm memoization as hash map
    * @param {string} s1
    * @param {string} s2
    * @param {string} s3
    * @return {boolean}
    */
   isInterleave(s1, s2, s3) {
      if (s1.length + s2.length !== s3.length) {
         return false
      }
      const memo = new Map();

      const dfs = (index1, index2) => {
         if (index1 + index2 === s3.length) {
            return true
         } else if (memo.has(`${index1},${index2}`)) {
            return false
         }

         const index = index1 + index2;
         if (
            index1 < s1.length &&
            s3[index] === s1[index1] &&
            dfs(index1 + 1, index2) 
         ) {
            return true
         }
         if (
            index2 < s2.length &&
            s3[index] === s2[index2] &&
            dfs(index1, index2 + 1) 
         ) {
            return true
         }
         memo.set(`${index1},${index2}`, false)
         return false
      }
      return dfs(0, 0)
   };
}
const isInterleave = new Solution().isInterleave;


console.log(new Solution().isInterleave('aa', 'bb', 'aabb') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac') === true)
console.log(new Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc') === false)
console.log(new Solution().isInterleave('', '', '') === true)
console.log(new Solution().isInterleave('cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc', 'abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb', 'abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb') === true)