class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} word
    * @return {number}
    */
   countSubstrings(word) {
      let palindromeCounter = 0;

      for (let index = 0; index < word.length; index++) {
         // check for odd length palindromes
         countPalindromes(index, index);
         // check for even length palindromes
         countPalindromes(index, index + 1);
      }
      return palindromeCounter;

      function countPalindromes(left, right) {
         while (
            left >= 0 &&
            right < word.length &&
            word[left] === word[right]
         ) {
            palindromeCounter++;
            left--;
            right++;
         }
      }
   };
}


console.log(new Solution().countSubstrings('abc'), 3)
console.log(new Solution().countSubstrings('aaa'), 6)