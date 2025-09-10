class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * text.slice(index + 1,)
    * @param {string} text
    * @return {string}
    */
   shortestPalindrome(text) {
      let palindrome = '';

      const isPalindrome = (left, right) => {
         while (left < right) {
            if (text[left] === text[right]) {
               left++;
               right--;
            } else {
               return false
            }
         }
         return true
      };

      for (let index = text.length - 1; index > -1; index--) {
         if (isPalindrome(0, index)) {
            palindrome = text.slice(index + 1,).split('').reverse().join('') + text
            break
         }
      }
      return palindrome
   };
}


console.log(new Solution().shortestPalindrome('aacecaaa') == 'aaacecaaa')
console.log(new Solution().shortestPalindrome('abcd') == 'dcbabcd')
console.log(new Solution().shortestPalindrome('') === '')