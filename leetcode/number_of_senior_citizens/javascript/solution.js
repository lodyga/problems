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
      let res = 0;

      for (const detail of details) {
         const c1 = detail[11];
         const c2 = detail[12];

         if (
            (c1 === '6' && c2 > '0') ||
            c1 > '6'
         ) {
            res++;
         }
      }

      return res;
   }
}


const countSeniors = new Solution().countSeniors;
console.log(new Solution().countSeniors(['7868190130M7522', '5303914400F9211', '9273338290F4010']) === 2)
console.log(new Solution().countSeniors(['1313579440F2036', '2921522980M5644']) === 0)
console.log(new Solution().countSeniors(['9751302862F0693', '3888560693F7262', '5485983835F0649', '2580974299F6042', '9976672161M6561', '0234451011F8013', '4294552179O6482']) === 4)
