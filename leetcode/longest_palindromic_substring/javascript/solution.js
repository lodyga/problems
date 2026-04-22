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
      let resLen = 1;
      let resStart = 0;

      const getPalindromeLen = (idx, d) => {
         let left = idx;
         let right = idx + d;

         while (
            left > -1 && right < text.length &&
            text[left] === text[right]
         ) {
            left--;
            right++;
         }

         return right - left - 1
      }

      // Check for odd length palindrome.
      for (let idx = 1; idx < text.length - 1; idx++) {
         const palLen = getPalindromeLen(idx, 0);

         if (palLen > resLen) {
            resLen = palLen;
            resStart = idx - Math.floor(resLen / 2);
         }
      }

      // Check for even length palindrome.
      for (let idx = 0; idx < text.length - 1; idx++) {
         const palLen = getPalindromeLen(idx, 1);

         if (palLen > resLen) {
            resLen = palLen;
            resStart = idx - Math.floor(resLen / 2) + 1;
         }
      }

      return text.slice(resStart, resStart + resLen)
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
