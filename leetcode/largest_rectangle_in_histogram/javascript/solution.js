class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * monotonic increasing stack
    * @param {number[]} heights
    * @return {number}
    */
   largestRectangleArea(heights) {
      const stack = [];  // [[index, height], ...]
      let area = 0;

      for (let index = 0; index < heights.length; index++) {
         const height = heights[index];
         let prevIndex = index;
         while (stack.length && stack[stack.length - 1][1] > height) {
            const [poppedIndex, prevHeight] = stack.pop();
            prevIndex = poppedIndex;
            area = Math.max(area, prevHeight * (index - prevIndex));
         }
         stack.push([prevIndex, height])

      }
      for (let index = stack.length - 1; index >= 0; index--) {
         const [prevIndex, prevHeight] = stack[index];
         area = Math.max(area, prevHeight * (heights.length - prevIndex));
      }
      return area
   };
}
const largestRectangleArea = new Solution().largestRectangleArea;


console.log(new Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) === 10)
console.log(new Solution().largestRectangleArea([2, 4]) === 4)
console.log(new Solution().largestRectangleArea([2, 1, 2]) === 3)