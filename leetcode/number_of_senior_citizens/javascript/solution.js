class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string[]} details
    * @return {number}
    */
   countSeniors(details) {
      let seniorCounter = 0;
      
      for (const detail of details) {
         const digit1 = detail[11];
         const digit2 = detail[12];

         if (
            '789'.includes(digit1) ||
            (digit1 === '6' && digit2 > '0')
         ) {
            seniorCounter++;
         }
      }
      return seniorCounter
   };
}


const countSeniors = new Solution().countSeniors;
console.log(new Solution().countSeniors(['7868190130M7522', '5303914400F9211', '9273338290F4010']) === 2)
console.log(new Solution().countSeniors(['1313579440F2036', '2921522980M5644']) === 0)
console.log(new Solution().countSeniors(['9751302862F0693', '3888560693F7262', '5485983835F0649', '2580974299F6042', '9976672161M6561', '0234451011F8013', '4294552179O6482']) === 4)
