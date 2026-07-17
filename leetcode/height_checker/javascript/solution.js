class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting
    * @param {number[]} heights 
    * @returns {number}
    */
   heightChecker(heights) {
      const sortedHeights = heights.slice().sort((a, b) => a - b);
      let res = 0;

      for (let idx = 0; idx < heights.length; idx++) {
         if (heights[idx] !== sortedHeights[idx]) {
            res++;
         }
      }

      return res;
   }
}


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
      const heightFreq = Array(100).fill(0);
      let res = 0;
      let idx = 0;

      for (const height of heights) {
         heightFreq[height - 1]++;
      }

      for (let height = 1; height < heightFreq.length + 1; height++) {
         const freq = heightFreq[height - 1];

         if (freq) {
            for (let i = 0; i < freq; i++) {
               if (height !== heights[idx]) {
                  res++;
               }

               idx++;
            }
         }
      }

      return res;
   }
}


const heightChecker = new Solution().heightChecker;
console.log(new Solution().heightChecker([1, 1, 4, 2, 1, 3]) === 3)
console.log(new Solution().heightChecker([5, 1, 2, 3, 4]) === 5)
console.log(new Solution().heightChecker([1, 2, 3, 4, 5]) === 0)
console.log(new Solution().heightChecker([10, 6, 6, 10, 10, 9, 8, 8, 3, 3, 8, 2, 1, 5, 1, 9, 5, 2, 7, 4, 7, 7]) === 22)
