class Solution {
   /**
    * Time complexity: O(n*k)
    *     k: word count
    *     n: avg word length
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: two pointers
    * @param {string[]} words
    * @return {string}
    */
   firstPalindrome(words) {
      const isPalindrome = (word) => {
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

      for (const word of words) {
         if (isPalindrome(word))
            return word
      }
      return ''
   };

   /**
    * Time complexity: O(n*k)
    *     k: word count
    *     n: avg word length
    * Auxiliary space complexity: O(k)
    * Tags: 
    *     A: two pointers, build-in function
    * @param {string[]} words
    * @return {string}
    */
   firstPalindrome(words) {
      for (const word of words) {
         if (word === word.split('').reverse().join(''))
            return word
      }
      return ''
   };
}


const firstPalindrome = new Solution().firstPalindrome;
console.log(new Solution().firstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool']) === 'ada')
console.log(new Solution().firstPalindrome(['notapalindrome', 'racecar']) === 'racecar')
console.log(new Solution().firstPalindrome(['def', 'ghi']) === '')
console.log(new Solution().firstPalindrome(['cqllrtyhw', 'swwisru', 'gpzmbders', 'wqibjuqvs', 'pp', 'usewxryy', 'ybqfuh', 'hqwwqftgyu', 'jggmatpk']) === 'pp')
