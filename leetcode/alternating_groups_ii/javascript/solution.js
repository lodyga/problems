class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {number[]} colors
    * @param {number} k
    * @return {number}
    */
   numberOfAlternatingGroups(colors, k) {
      const N = colors.length;
      let prev_color = -1;
      let left = 0;
      let counter = 0;

      // Right exclude the last element in the second loop
      // to avoid duplicate group ending in the last element of colors.
      for (let right = 0; right < 2 * N - 1; right++) {
         const color = colors[right % N];

         if (color === prev_color) {
            left = right;
            // If left start the second loop then break.
            if (left >= N)
               break
            continue
         }

         prev_color = color;

         // If group lenght is to short.
         if (right - left + 1 < k)
            continue

         // If left start the second loop then break.
         if (left === N)
            break
         left += 1;

         counter += 1;
      }
      return counter
   };
}


const numberOfAlternatingGroups = new Solution().numberOfAlternatingGroups;
console.log(new Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) === 3)
console.log(new Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6) === 2)
console.log(new Solution().numberOfAlternatingGroups([1, 1, 0, 1], 4) === 0)
console.log(new Solution().numberOfAlternatingGroups([0, 1, 1], 3) === 1)
console.log(new Solution().numberOfAlternatingGroups([0, 1, 0, 1], 3) === 4)
console.log(new Solution().numberOfAlternatingGroups([0, 0, 1, 0, 0], 3) === 1)
console.log(new Solution().numberOfAlternatingGroups([0, 0, 1, 0, 1], 3) === 3)
