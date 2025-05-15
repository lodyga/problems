class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} heights
    * @return {number}
    */
   maxArea(heights) {
      let maxWaterArea = 0;
      let left = 0;
      let right = heights.length - 1;

      while (left < right) {
         let area = (right - left) * Math.min(heights[left], heights[right]);
         maxWaterArea = Math.max(maxWaterArea, area);

         if (heights[left] < heights[right]) {
            left++;
         } else {
            right--;
         }
      }
      return maxWaterArea
   };
}


console.log(new Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) === 49)
console.log(new Solution().maxArea([1, 1]) === 1)
console.log(new Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) === 17)