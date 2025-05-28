class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {string} text
    * @return {number}
    */
   minFlips(text) {
      let left = 0;
      const textLength = text.length;
      let flip01 = 0;
      let flip10 = 0;
      let minFlips = textLength;

      for (let right = 0; right < textLength * 2; right++) {
         const digit = text[right % textLength];

         if (digit == right % 2) {
            flip10++;
         } else {
            flip01++;
         }

         if (right - left + 1 === textLength) {
            minFlips = Math.min(minFlips, flip01, flip10);

            // early exit when there are no flips
            if (minFlips === 0) {
               return 0
            }
            if (text[left % textLength] == left % 2) {
               flip10--;
            } else {
               flip01--;
            }
            left++;
         }
      }
      return minFlips
   };
}
const minFlips = new Solution().minFlips;


console.log(new Solution().minFlips('111000') === 2)
console.log(new Solution().minFlips('010') === 0)
console.log(new Solution().minFlips('1110') === 1)
console.log(new Solution().minFlips('01001001101') === 2)