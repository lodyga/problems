class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: counting sort
    * @param {number[]} heights
    * @return {number}
    */
   heightChecker(heights) {
      const heightBucket = Array(100).fill(0);
      for (const height of heights) {
         heightBucket[height - 1] += 1;
      }

      const sortedHeights = [];
      for (let index = 0; index < heightBucket.length; index++) {
         for (let i = 0; i < heightBucket[index]; i++) {
            sortedHeights.push(index + 1);
         }
      }

      let missmatch = 0;
      for (let index = 0; index < heights.length; index++) {
         if (heights[index] !== sortedHeights[index]) {
            missmatch++;
         }
      }
      return missmatch
   };
}


const heightChecker = new Solution().heightChecker;
console.log(new Solution().heightChecker([1, 1, 4, 2, 1, 3]) === 3)
console.log(new Solution().heightChecker([5, 1, 2, 3, 4]) === 5)
console.log(new Solution().heightChecker([1, 2, 3, 4, 5]) === 0)
