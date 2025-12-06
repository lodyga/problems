class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: iteration
    * @param {number[]} heights
    * @return {number}
    */
   largestRectangleArea(heights) {
      const heightStack = [];  // [[index, height], ...]
      let maxArea = heights[0];

      for (let index = 0; index < heights.length; index++) {
         const height = heights[index];
         let start = index;

         while (heightStack.length && heightStack[heightStack.length - 1][1] > height) {
            const [poppedIndex, prevHeight] = heightStack.pop();
            start = poppedIndex;
            maxArea = Math.max(maxArea, prevHeight * (index - start));
         }
         heightStack.push([start, height]);

      }
      for (const [index, height] of heightStack) {
         maxArea = Math.max(maxArea, height * (heights.length - index));
      }
      return maxArea
   };
}


const largestRectangleArea = new Solution().largestRectangleArea;
console.log(new Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) === 10)
console.log(new Solution().largestRectangleArea([2, 4]) === 4)
console.log(new Solution().largestRectangleArea([2, 1, 2]) === 3)
