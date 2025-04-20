class Solution {
   /**
    * Time complexity: O(k*n)
    *     k: word count
    *     n: average word length
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string[]} words
    * @return {string}
    */
   firstPalindrome(words) {
      for (const word of words) {
         if (this.isPalindrome(word))
            return word
      }
      return ''
   };

   isPalindrome(word) {
      let left = 0;
      let right = word.length - 1;

      while (left < right) {
         if (word[left] !== word[right])
            return false
         left++;
         right--;
      }

      return true
   };

   /**
    * Time complexity: O(k*n)
    *     k: word count
    *     n: average word length
    * Auxiliary space complexity: O(n)
    * Algorithm: build-in function
    * @param {string[]} words
    * @return {string}
    */
   firstPalindromeUsingBuindIn(words) {
      for (const word of words) {
         if (word === word.split('').reverse().join(''))
            return word
      }
      return ''
   };
}


console.log(new Solution().firstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool']), 'ada')
console.log(new Solution().firstPalindrome(['notapalindrome', 'racecar']), 'racecar')
console.log(new Solution().firstPalindrome(['def', 'ghi']), '')