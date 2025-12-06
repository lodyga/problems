class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: build-in function
    * @param {string} text
    * @return {string}
    */
   reverseWords(text) {
      return text
         .split(' ')
         .reverse()
         .join(' ')
         .split('')
         .reverse()
         .join('')
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: two pointers
    * @param {string} text
    * @return {string}
    */
   reverseWords(text) {
      const reverseWord = (left, right) => {
         while (left < right) {
            [letters[left], letters[right]] = [letters[right], letters[left]];
            left += 1;
            right -= 1;
         }
      };

      const letters = Array.from(text);
      let left = 0;
      for (let right = 0; right < text.length; right++) {
         const letter = letters[right];
         if (letter === ' ' || right === text.length - 1) {
            reverseWord(left, right == text.length - 1 ? right : right - 1)
            left = right + 1;
         }
      }
      return letters.join('')
   };
}


const reverseWords = new Solution().reverseWords;
console.log(new Solution().reverseWords('Let\'s take LeetCode contest') == 's\'teL ekat edoCteeL tsetnoc')
console.log(new Solution().reverseWords('Mr Ding') == 'rM gniD')
console.log(new Solution().reverseWords('hehhhhhhe') == 'ehhhhhheh')
