class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down
    *     regex
    * @param {str} text
    * @param {str} pattern
    * @return {boolean}
    */
   isMatch(text, pattern) {
      const memo = Array.from({ length: text.length + 1 }, () => Array(pattern.length).fill(-1));

      const dfs = (index1, index2) => {
         if (index2 === pattern.length) {
            return index1 === text.length
         } else if (memo[index1][index2] !== -1) {
            return memo[index1][index2]
         }

         const isLetterMatched = index1 < text.length && (pattern[index2] === '.' || pattern[index2] === text[index1]);
         const isStarNext = pattern[index2 + 1] === "*";

         let res = 0
         if (isStarNext) {
            // Skip current pattrn.
            if (dfs(index1, index2 + 2)) {
               res = 1;
            }
            // if letter matched and use parrtern
            else if (isLetterMatched && dfs(index1 + 1, index2)) {
               res = 1;
            }
         } else if (isLetterMatched) {
            res = dfs(index1 + 1, index2 + 1);
         }

         memo[index1][index2] = res;
         return res
      }
      return Boolean(dfs(0, 0))
   };
}


const isMatch = new Solution().isMatch;
console.log(new Solution().isMatch('a', 'a') === true)
console.log(new Solution().isMatch('aa', 'a') === false)
console.log(new Solution().isMatch('a', 'aa') === false)
console.log(new Solution().isMatch('aa', 'a*') === true)
console.log(new Solution().isMatch('ab', 'a*') === false)
console.log(new Solution().isMatch('aaaaa', 'a*') === true)
console.log(new Solution().isMatch('ab', '.*') === true)
console.log(new Solution().isMatch('b', 'a*b') === true)
console.log(new Solution().isMatch('ab', 'a*b') === true)
console.log(new Solution().isMatch('aab', 'c*a*b') === true)
console.log(new Solution().isMatch('ippi', 'p*.') === false)
console.log(new Solution().isMatch('mississippi', 'mis*is*p*.') === false)
console.log(new Solution().isMatch('ipp', 'ip*') === true)
console.log(new Solution().isMatch('ippi', 'ip*.') === true)
console.log(new Solution().isMatch('mississippi', 'mis*is*ip*.') === true)
console.log(new Solution().isMatch('', 'b*') === true)
console.log(new Solution().isMatch('ab', '.*c') === false)
console.log(new Solution().isMatch('abc', '.*c') === true)
console.log(new Solution().isMatch('aaa', 'a*a') === true)
console.log(new Solution().isMatch('aabcbcbcaccbcaabc', '.*a*aa*.*b*.c*.*a*') === true)
