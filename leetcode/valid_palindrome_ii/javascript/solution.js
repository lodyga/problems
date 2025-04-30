class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} word
    * @return {boolean}
    */
   validPalindrome(word) {
      function isPalindrome(left, right) {
         while (left < right) {
            if (word[left] != word[right])
               return false
            left++;
            right--;
         }
         return true
      };

      let left = 0;
      let right = word.length - 1;

      while (left < right) {
         if (word[left] === word[right]) {
            left++;
            right--;
         } else {
            return (
               isPalindrome(left + 1, right) || 
               isPalindrome(left, right - 1)
            )
         }
      }
      return true
   };
}


console.log(new Solution().validPalindrome('aba') == true)
console.log(new Solution().validPalindrome('abca') == true)
console.log(new Solution().validPalindrome('abc') == false)
console.log(new Solution().validPalindrome('deeee') == true)
console.log(new Solution().validPalindrome('eeccccbebaeeabebccceea') == false)
console.log(new Solution().validPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga') == true)