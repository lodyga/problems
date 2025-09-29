class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Rabin-Karp
    * @param {string} text
    * @return {string}
    */
   shortestPalindrome(text) {
      const BASE = 29;
      const MOD = 10 ** 9 + 7;
      let power = 1;
      let prefix = 0;
      let postfix = 0;
      let lastIndex = 0;

      for (let index = 0; index < text.length; index++) {
         const value = text[index].charCodeAt(0) - 'a'.charCodeAt(0);
         prefix = (prefix * BASE + value) % MOD;
         postfix = (postfix + value * power) % MOD
         power = (power * BASE) % MOD;

         if (prefix === postfix)
            lastIndex = index;
      }
      return text.slice(lastIndex + 1,).split('').reverse().join('') + text
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers, tle
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


const shortestPalindrome = new Solution().shortestPalindrome;
console.log(new Solution().shortestPalindrome('aacecaaa') === 'aaacecaaa')
console.log(new Solution().shortestPalindrome('abcd') === 'dcbabcd')
console.log(new Solution().shortestPalindrome('') === '')