class Solution {
   /**
    * Time complexity: O(logn)
    *     log (base = 26) n
    * Auxiliary space complexity: O(logn)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {number} colNum
    * @return {string}
    */
   convertToTitle(colNum) {
      let colName = [];

      while (colNum > 0) {
         const mod = (colNum - 1) % 26;
         const char = String.fromCharCode('A'.charCodeAt() + mod)
         colName.push(char);
         colNum = Math.floor((colNum - 1) / 26);
      }
      return colName.reverse().join('');
   };
}


const convertToTitle = new Solution().convertToTitle;
console.log(new Solution().convertToTitle(1) === 'A')
console.log(new Solution().convertToTitle(26) === 'Z')
console.log(new Solution().convertToTitle(27) === 'AA')
console.log(new Solution().convertToTitle(28) === 'AB')
console.log(new Solution().convertToTitle(51) === 'AY')
console.log(new Solution().convertToTitle(52) === 'AZ')
console.log(new Solution().convertToTitle(53) === 'BA')
console.log(new Solution().convertToTitle(54) === 'BB')
console.log(new Solution().convertToTitle(701) === 'ZY')
console.log(new Solution().convertToTitle(2147483647) === 'FXSHRXW')
