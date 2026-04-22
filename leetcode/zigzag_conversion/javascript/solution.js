class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string, array
    *     A: iteration
    * @param {string} text
    * @param {number} numRows
    * @return {string}
    */
   convert(text, numRows) {
      if (numRows === 1) {
         return text
      }

      const res = Array.from({ length: numRows }, () => '');

      for (let index = 0; index < text.length; index++) {
         const letter = text[index];
         const row = index % (2 * (numRows - 1));
         let newIndex;

         if (row < numRows) {
            newIndex = row;
         } else {
            newIndex = 2 * (numRows - 1) - row;
         }

         res[newIndex] = res[newIndex] + letter;
      }

      return res.join('')
   };
}


const convert = new Solution().convert;
console.log(new Solution().convert('PAYPALISHIRING', 3) === 'PAHNAPLSIIGYIR')
console.log(new Solution().convert('PAYPALISHIRING', 4) === 'PINALSIGYAHRPI')
console.log(new Solution().convert('A', 1) === 'A')
