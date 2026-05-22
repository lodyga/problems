class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
     * @param {string} subSeq
     * @param {string} text
     * @return {boolean}
    */
   isSubsequence(subSeq, text) {
      if (subSeq === '') return true
      let idx = 0;

      for (const letter of text) {
         if (letter === subSeq[idx]) {
            idx++;
            
            if (idx === subSeq.length)
               return true
         }
      }

      return false
   }
}


const isSubsequence = new Solution().isSubsequence;
console.log(new Solution().isSubsequence('abc', 'ahbgdc') === true)
console.log(new Solution().isSubsequence('axc', 'ahbgdc') === false)
console.log(new Solution().isSubsequence('', 'ahbgdc') === true)
console.log(new Solution().isSubsequence('', '') === true)
