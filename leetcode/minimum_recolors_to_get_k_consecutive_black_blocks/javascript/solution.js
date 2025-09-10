class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {str} blocks
    * @param {number} windowLength
    * @return {number}
    */
   static minimumRecolors(blocks, windowLength) {
      let window = 0;
      let maxWindow = 0;
      
      for (let index = 0; index < windowLength; index++) {
         if (blocks[index] === 'B') {
            window++;
            maxWindow++;
         }
      }

      for (let right = windowLength; right < blocks.length; right++) {
         const left = right - windowLength;
         if (blocks[left] === 'B')
            window--
         if (blocks[right] === 'B')
            window++
         maxWindow = Math.max(maxWindow, window);
         if (maxWindow === windowLength)
            return 0
      }
      return windowLength - maxWindow
   };
}
const minimumRecolors = Solution.minimumRecolors;


console.log(minimumRecolors('WBBWWBBWBW', 7) === 3)
console.log(minimumRecolors('WBWBBBW', 2) === 0)