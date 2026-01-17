class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {string[]} text
    * @return {string[]}
    */
   longestPalindrome(text) {
      let palindromeLength = 0;
      let longestPalindromeLength = 0;
      let start = 0;

      const checkForPalindrome = (left, right) => {
         while (
            left > -1 &&
            right < text.length &&
            text[left] === text[right]
         ) {
            palindromeLength = right - left + 1;
            if (palindromeLength > longestPalindromeLength) {
               longestPalindromeLength = palindromeLength;
               start = left;
            }
            left--;
            right++;
         }
      }

      for (let index = 0; index < text.length; index++) {
         // check for odd length palindrome
         checkForPalindrome(index, index)
         // check for even length palindrome
         checkForPalindrome(index, index + 1)
      }
      return text.slice(start, start + longestPalindromeLength)
   };
}


const longestPalindrome = new Solution().longestPalindrome
console.log(new Solution().longestPalindrome('babad') === 'bab')
console.log(new Solution().longestPalindrome('cbbd') === 'bb')
console.log(new Solution().longestPalindrome('a') === 'a')
console.log(new Solution().longestPalindrome('') === '')
console.log(new Solution().longestPalindrome('bb') === 'bb')
console.log(new Solution().longestPalindrome('ab') === 'a')
console.log(new Solution().longestPalindrome('aacabdkacaa') === 'aca')
console.log(new Solution().longestPalindrome('abdka') === 'a')
console.log(new Solution().longestPalindrome('aaaa') === 'aaaa')
