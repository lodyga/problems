class Solution {
   /**
    * Time complexity: O(n*m)
    *     n: bank row count
    *     m: bank col count
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string[]} bank
    * @return {number}
    */
   numberOfBeams(bank) {
      let beams = 0;
      let prevDevices = 0;
      
      for (const row of bank) {
         let lasers = row.split('').filter(char => char === '1').length;
         
         if (lasers) {
            beams += prevDevices * lasers;
            prevDevices = lasers;
         }
      }
      return beams
   };
}


const numberOfBeams = new Solution().numberOfBeams;
console.log(new Solution().numberOfBeams(['11', '11']) === 4)
console.log(new Solution().numberOfBeams(['000', '111', '000']) === 0)
console.log(new Solution().numberOfBeams(['011001', '000000', '010100', '001000']) === 8)
