class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {number[]} heights
    * @return {number}
    */
   maxArea(heights) {
      let res = 0;
      let left = 0;
      let right = heights.length - 1;

      while (left < right) {
         const leftHeight = heights[left];
         const rightHeight = heights[right];

         const height = Math.min(leftHeight, rightHeight)
         const width = right - left;
         res = Math.max(res, height * width);

         heights[left] < heights[right] ? left++ : right--;
      }

      return res
   };
}


const maxArea = new Solution().maxArea;
console.log(new Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) === 49)
console.log(new Solution().maxArea([1, 1]) === 1)
console.log(new Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) === 17)
