class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: two pointers
    * @param {number[]} heights
    * @return {number}
    */
   trap(heights) {
      let left = 0;
      let right = heights.length - 1;
      let leftMax = 0;
      let rightMax = 0;
      let res = 0;

      while (left < right) {
         const leftHeight = heights[left];
         const rightHeight = heights[right];

         if (leftHeight < rightHeight) {
            leftMax = Math.max(leftMax, leftHeight);
            res += leftMax - leftHeight;
            left++;
         } else {
            rightMax = Math.max(rightMax, rightHeight);
            res += rightMax - rightHeight;
            right--;
         }
      }
      
      return res
   };
}


const trap = new Solution().trap;
console.log(new Solution().trap([3, 1, 2]) === 1)
console.log(new Solution().trap([5, 8]) === 0)
console.log(new Solution().trap([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) === 8)
console.log(new Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) === 6)
console.log(new Solution().trap([4, 2, 0, 3, 2, 5]) === 9)
