class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: two pointers
    * @param {number[]} heights
    * @return {number}
    */
   floodDepth(heights) {
      let left = 0;
      let right = heights.length - 1;
      let maxLeftHeight = heights[0];
      let maxRightHeight = heights[right];
      let maxDepth = 0;

      while (left < right) {
         const leftHeight = heights[left];
         const rightHeight = heights[right];
         let depth = 0;

         if (leftHeight < rightHeight) {
            maxLeftHeight = Math.max(maxLeftHeight, leftHeight);
            depth = maxLeftHeight - leftHeight;
            left++;
         } else {
            maxRightHeight = Math.max(maxRightHeight, rightHeight);
            depth = maxRightHeight - rightHeight;
            right--;
         }
         maxDepth = Math.max(maxDepth, depth);
      }
      return maxDepth
   };
}


const floodDepth = new Solution().floodDepth;
console.log(floodDepth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) === 2)
console.log(floodDepth([5, 8]) === 0)
console.log(floodDepth([3, 1, 2]) === 1)
console.log(floodDepth([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) === 2)
