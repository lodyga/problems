class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    * @param {string[]} details
    * @return {number}
    */
   countSeniors(details) {
      let seniorCounter = 0;
      
      for (const detail of details) {
         const digit1 = detail[11];
         const digit2 = detail[12];

         if (
            digit1 > '6' ||
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