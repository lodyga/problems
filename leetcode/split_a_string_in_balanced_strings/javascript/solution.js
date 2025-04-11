class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {string} sides
    * @return {number}
    */
   balancedStringSplit(sides) {
      let sideCounter = 0;
      let balancedStringCounter = 0;

      for (const side of sides) {
         if (side === 'R') {
            sideCounter++;
         } else {
            sideCounter--;
         }
         if (sideCounter === 0) {
            balancedStringCounter++;
         }
      }
      return balancedStringCounter
   }
}


console.log(new Solution().balancedStringSplit('RLRRLLRLRL'), 4)
console.log(new Solution().balancedStringSplit('RLRRRLLRLL'), 2)
console.log(new Solution().balancedStringSplit('LLLLRRRR'), 1)