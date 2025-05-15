class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string[]} word
    * @return {string[]}
    */
   longestPalindrome(word) {
      let palindromeLength = 0;
      let start = 0;

      for (let index = 0; index < word.length; index++) {
         // check for odd length palindrome
         checkForPalindrome(index, index)
         // check for even length palindrome
         checkForPalindrome(index, index + 1)
      }

      function checkForPalindrome(left, right) {
         while (
            left >= 0 &&
            right < word.length &&
            word[left] === word[right]
         ) {
            left--;
            right++;
         }
         if (right - left - 1 > palindromeLength) {
            palindromeLength = right - left - 1;
            start = left + 1
         }
      }

      return word.slice(start, start + palindromeLength)
   };
}


console.log(new Solution().longestPalindrome('babad'), 'bab')
console.log(new Solution().longestPalindrome('a'), 'a')
console.log(new Solution().longestPalindrome('cbbd'), 'bb')
console.log(new Solution().longestPalindrome(''), '')
console.log(new Solution().longestPalindrome('bb'), 'bb')
console.log(new Solution().longestPalindrome('ab'), 'a')
console.log(new Solution().longestPalindrome('aacabdkacaa'), 'aca')
console.log(new Solution().longestPalindrome('abdka'), 'a')
console.log(new Solution().longestPalindrome('aaaa'), 'aaaa')