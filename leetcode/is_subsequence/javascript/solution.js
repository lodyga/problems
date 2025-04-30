class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
     * @param {string} s
     * @param {string} t
     * @return {boolean}
    */
   isSubsequence(word1, word2) {
      if (word1.length === 0)
         return true

      let left = 0;

      for (let right = 0; right < word2.length; right++) {
         if (word2[right] === word1[left]) {
            left++;
         }
         if (left === word1.length)
            return true
      }

      return false
   };
}


console.log(new Solution().isSubsequence("", ""), true)
console.log(new Solution().isSubsequence("", "ahbgdc"), true)
console.log(new Solution().isSubsequence("abc", "ahbgdc"), true)
console.log(new Solution().isSubsequence("axc", "ahbgdc"), false)