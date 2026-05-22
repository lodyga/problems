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
      const stack = [];

      for (const char of text) {
         if (stack.length && char === '*') {
            stack.pop();
         } else {
            stack.push(char);
         }
      }

      return stack.join('');
   }
}


const removeStars = new Solution().removeStars;
console.log(new Solution().removeStars('leet**cod*e') === 'lecoe')
console.log(new Solution().removeStars('erase*****') === '')
