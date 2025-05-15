/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(1)
 * Tags: two pointers
 * @param {number[]} heights
 * @return {number}
 */
function floodDepth(heights) {
   let maxDepth = 0;
   let left = 0;
   let right = heights.length - 1;
   let leftWall = heights[0];
   let rightWall = heights[right];

   while (left < right) {
      const leftHeight = heights[left];
      const rightHeight = heights[right];

      if (leftHeight < rightHeight) {
         leftWall = Math.max(leftWall, leftHeight);
         const depth = leftWall - leftHeight;
         maxDepth = Math.max(maxDepth, depth);
         left++;
      } else {
         rightWall = Math.max(rightWall,rightHeight);
         const depth = rightWall -rightHeight;
         maxDepth = Math.max(maxDepth, depth);
         right--;
      }
   }
   return maxDepth
};


console.log(floodDepth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) === 2)
console.log(floodDepth([5, 8]) === 0)
console.log(floodDepth([3, 1, 2]) === 1)
console.log(floodDepth([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) === 2)