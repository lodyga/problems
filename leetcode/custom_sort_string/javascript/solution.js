class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bucket sort
    * @param {string} order
    * @param {string} s
    * @return {string}
    */
   customSortString(order, s) {
      const orderPositionByChar = Array(26).fill(-1);
      const orderedChars = Array(26).fill('');
      const unorderedChars = [];

      for (let index = 0; index < order.length; index++) {
         const letterIndex = order.charCodeAt(index) - 'a'.charCodeAt(0);
         orderPositionByChar[letterIndex] = index;
      }

      for (const char of s) {
         const letterIndex = char.charCodeAt(0) - 'a'.charCodeAt(0);
         const index = orderPositionByChar[letterIndex];

         if (index === -1) {
            unorderedChars.push(char);
         } else {
            orderedChars[index] = orderedChars[index] + char;
         }
      }

      return orderedChars.join('') + unorderedChars.join('')
   };
}


const customSortString = new Solution().customSortString;
console.log(new Solution().customSortString('cba', 'abcd') === 'cbad')
console.log(new Solution().customSortString('bcafg', 'abcd') === 'bcad')
