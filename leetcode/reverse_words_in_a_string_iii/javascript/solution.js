class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} text
    * @return {string}
    */
   reverseWords(text) {
      const letterList = [];
      const textWithReversedWords = [];

      for (const letter of text + ' ') {
         if (letter == ' ') {
            textWithReversedWords.push(...letterList.reverse());
            textWithReversedWords.push(' ');
            letterList.length = 0;
         } else {
            letterList.push(letter);
         }
      }
      return textWithReversedWords
         .slice(0, textWithReversedWords.length - 1)
         .join('')
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tag: build-in function
    * @param {string} text
    * @return {string}
    */
   reverseWords2(text) {
      return text
         .split(' ')
         .reverse()
         .join(' ')
         .split('')
         .reverse()
         .join('')
   };
}


console.log(new Solution().reverseWords2('Let\'s take LeetCode contest'), 's\'teL ekat edoCteeL tsetnoc')
console.log(new Solution().reverseWords2('Mr Ding'), 'rM gniD')
console.log(new Solution().reverseWords2('hehhhhhhe'), 'ehhhhhheh')