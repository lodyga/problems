class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack
    *     A: iteration
    * @param {string} text
    * @return {string}
    */
   removeStars(text) {
      const letterStack = [];

      for (const char of text) {
         if (letterStack.length && char === '*')
            letterStack.pop();
         else
            letterStack.push(char);
      }
      return letterStack.join('')
   };
}


const removeStars = new Solution().removeStars;
console.log(new Solution().removeStars('leet**cod*e') === 'lecoe')
console.log(new Solution().removeStars('erase*****') === '')
