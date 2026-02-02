class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {str} blocks
    * @param {number} k
    * @return {number}
    */
   static minimumRecolors(blocks, k) {
      let window = 0;
      let minWindow = k;
      let left = 0;

      for (let right = 0; right < blocks.length; right++) {
         if (blocks[right] == 'W')
            window += 1;

         if (right < k - 1)
            continue

         minWindow = Math.min(minWindow, window);
         if (minWindow === 0)
            break

         if (blocks[left] == 'W')
            window -= 1;

         left += 1;
      }
      return minWindow
   };
}


const minimumRecolors = Solution.minimumRecolors;
console.log(minimumRecolors('WBBWWBBWBW', 7) === 3)
console.log(minimumRecolors('WBWBBBW', 2) === 0)
