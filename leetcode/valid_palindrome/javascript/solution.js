class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {string} text
    * @return {boolean}
    */
   static isPalindrome(text) {
      let left = 0;
      let right = text.length - 1;
      while (left < right) {
         while (
            left < right &&
            !isAlnum(text[left])
         ) {
            left++;
         }
         while (
            left < right &&
            !isAlnum(text[right])
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
   };

   /**
    * Check if character is a alpha-numeric.
    * @param {string} char
    * @return {boolean}
    */
   static isAlnum(char) {
      const isLower = (char >= 'a' && char <= 'z');
      const isUpper = (char >= 'A' && char <= 'Z');
      const isNumber = (char >= '0' && char <= '9');
      return (isLower || isUpper || isNumber)
   };
}


class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, build-in function
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


const isPalindrome = Solution.isPalindrome;
const isAlnum = Solution.isAlnum;
console.log(new Solution().isPalindrome('A man, a plan, a canal: Panama') === true)
console.log(new Solution().isPalindrome('race a car') === false)
console.log(new Solution().isPalindrome(' ') === true)
console.log(new Solution().isPalindrome('0P') === false)
console.log(new Solution().isPalindrome('ab_a') === true)
console.log(new Solution().isPalindrome('a,,') === true)
