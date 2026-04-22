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
      const res = [];
      const stack = [];

      for (let char of text + ' ') {
         if (char === ' ') {
            res.push(stack.reverse().join(''))
            stack.length = 0;
         } else {
            stack.push(char);
         }
      }
      
      return res.join(' ')
   };
}


const reverseWords = new Solution().reverseWords;
console.log(new Solution().reverseWords('Let\'s take LeetCode contest') == 's\'teL ekat edoCteeL tsetnoc')
console.log(new Solution().reverseWords('Mr Ding') == 'rM gniD')
console.log(new Solution().reverseWords('hehhhhhhe') == 'ehhhhhheh')
