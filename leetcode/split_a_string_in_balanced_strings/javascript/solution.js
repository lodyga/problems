class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   balancedStringSplit(sides) {
      let surplus = 0;
      let counter = 0;

      for (const side of sides) {
         side === 'R' ? surplus++ : surplus--;
         if (surplus === 0) {
            counter++;
         }
      }
      return counter
   };
}


const balancedStringSplit = new Solution().balancedStringSplit;
console.log(new Solution().balancedStringSplit('RLRRLLRLRL') === 4)
console.log(new Solution().balancedStringSplit('RLRRRLLRLL') === 2)
console.log(new Solution().balancedStringSplit('LLLLRRRR') === 1)
