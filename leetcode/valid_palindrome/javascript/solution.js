class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} text
    * @return {boolean}
    */
   isPalindrome(text) {
      let left = 0;
      let right = text.length - 1;
      while (left < right) {
         while (
            left < right &&
            this.isPunctuation(text[left])
         ) {
            left++;
         }
         while (
            left < right &&
            this.isPunctuation(text[right])
         ) {
            right--;
         }
         if (text[left].toLowerCase() != text[right].toLowerCase()) {
            return false
         } else {
            left++;
            right--;
         }
      }
      return true
   }

   /**
    * Check if character is a punctuation.
    * @param {string} char
    * @return {boolean}
    */
   isPunctuation(char) {
      return !(
         (char >= '0' &&
            char <= '9') ||
         (char.toLowerCase() >= 'a' &&
            char.toLowerCase() <= 'z')
      )
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, regex
    * @param {string} text
    * @return {boolean}
    */
   isPalindrome(text) {
      let left = 0;
      let right = text.length - 1;
      while (left < right) {
         while (
            left < right &&
            text[left].match(/[\W_]/)
         ) {
            left++;
         }
         while (
            left < right &&
            text[right].match(/[\W_]/)
         ) {
            right--;
         }
         if (text[left].toLowerCase() != text[right].toLowerCase()) {
            return false
         } else {
            left++;
            right--;
         }
      }
      return true
   }
}


console.log(new Solution().isPalindrome('A man, a plan, a canal: Panama'), true)
console.log(new Solution().isPalindrome('race a car'), false)
console.log(new Solution().isPalindrome(' '), true)
console.log(new Solution().isPalindrome('0P'), false)
console.log(new Solution().isPalindrome('ab_a'), true)