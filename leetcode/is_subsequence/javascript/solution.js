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
      if (subSeq === '')
         return true

      let left = 0;
      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         if (letter === subSeq[left]) {
            left++;
            if (left === subSeq.length)
               return true
         }
      }
      return false
   };
}


const isSubsequence = new Solution().isSubsequence;
console.log(new Solution().isSubsequence('abc', 'ahbgdc') === true)
console.log(new Solution().isSubsequence('axc', 'ahbgdc') === false)
console.log(new Solution().isSubsequence('', 'ahbgdc') === true)
console.log(new Solution().isSubsequence('', '') === true)
