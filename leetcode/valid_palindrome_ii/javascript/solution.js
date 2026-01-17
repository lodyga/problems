class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {string} text
    * @return {boolean}
    */
   validPalindrome(text) {
      const validate = (left, right, joker) => {
         while (left < right) {
            if (text[left] === text[right]) {
               left++;
               right--;
            } else if (joker) {
               return (
                  validate(left + 1, right) ||
                  validate(left, right - 1)
               )
            } else {
               return false
            }
         }
         return true
      }
      return validate(0, text.length - 1, true)
   };
}


const validPalindrome = new Solution().validPalindrome;
console.log(new Solution().validPalindrome('aba') === true)
console.log(new Solution().validPalindrome('abca') === true)
console.log(new Solution().validPalindrome('abc') === false)
console.log(new Solution().validPalindrome('deeee') === true)
console.log(new Solution().validPalindrome('eeccccbebaeeabebccceea') === false)
console.log(new Solution().validPalindrome('abzzbab') === true)
console.log(new Solution().validPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga') === true)
