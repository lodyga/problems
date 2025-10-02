class Solution {
   /**
    * Time complexity: O(n * m)
    *     n: bank rows
    *     m: bank cols
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string[]} bank
    * @return {number}
    */
   numberOfBeams(bank) {
      let lasers = 0;
      let prevRowLasers = bank[0].split('').filter(char => char === '1').length;
      for (let index = 1; index < bank.length; index++) {
         let rowLasers = bank[index].split('').filter(char => char === '1').length;
         if (rowLasers) {
            lasers += prevRowLasers * rowLasers;
            prevRowLasers = rowLasers;
         }
      }
      return lasers
   };
}


const numberOfBeams = new Solution().numberOfBeams;
console.log(new Solution().numberOfBeams(['11', '11']) === 4)
console.log(new Solution().numberOfBeams(['011001', '000000', '010100', '001000']) === 8)
console.log(new Solution().numberOfBeams(['000', '111', '000']) === 0)