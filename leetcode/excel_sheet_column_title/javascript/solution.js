class Solution {
   /**
    * Time complexity: O(logn)
    *     log (base = 26) n
    * Auxiliary space complexity: O(1)
    * Tags: string
    * @param {number} columnNumber
    * @return {string}
    */
   convertToTitle(columnNumber) {
      let columnName = '';

      while (columnNumber > 0) {
         const mod = (columnNumber - 1) % 26;
         columnName = String.fromCharCode('A'.charCodeAt() + mod) + columnName;
         columnNumber = (columnNumber - 1) / 26 | 0;
      }
      return columnName
   };
}
const convertToTitle = new Solution().convertToTitle;


console.log(new Solution().convertToTitle(1) === 'A')
console.log(new Solution().convertToTitle(26) === 'Z')
console.log(new Solution().convertToTitle(28) === 'AB')
console.log(new Solution().convertToTitle(701) === 'ZY')