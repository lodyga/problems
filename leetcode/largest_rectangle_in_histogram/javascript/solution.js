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
      const heightStack = [];  // [[height, idx], ...]
      let res = heights[0];

      for (let idx = 0; idx < heights.length; idx++) {
         const height = heights[idx];
         let startIdx = idx;

         while (heightStack.length && heightStack[heightStack.length - 1][0] > height) {
            const [prevHeight, prevIdx] = heightStack.pop();
            startIdx = prevIdx;
            const width = idx - prevIdx;
            res = Math.max(res, prevHeight * width);
         }

         heightStack.push([height, startIdx]);
      }

      for (const [height, idx] of heightStack) {
         res = Math.max(res, height * (heights.length - idx));
      }

      return res;
   }
}


const largestRectangleArea = new Solution().largestRectangleArea;
console.log(new Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) === 10)
console.log(new Solution().largestRectangleArea([2, 4]) === 4)
console.log(new Solution().largestRectangleArea([2, 1, 2]) === 3)
