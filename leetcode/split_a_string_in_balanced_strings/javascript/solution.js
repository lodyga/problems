class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   balancedStringSplit(text) {
      let counter = 0;
      let res = 0;

      for (const side of text) {
         side === 'R' ? counter++ : counter--;
         if (counter === 0) res++;
      }
      
      return res
   };
}


const balancedStringSplit = new Solution().balancedStringSplit;
console.log(new Solution().balancedStringSplit('RLRRLLRLRL') === 4)
console.log(new Solution().balancedStringSplit('RLRRRLLRLL') === 2)
console.log(new Solution().balancedStringSplit('LLLLRRRR') === 1)
