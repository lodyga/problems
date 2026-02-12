class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {number[]} points
    * @param {number} k
    * @return {number}
    */
   maxScore(points, k) {
      const N = points.length;
      const numSum = points.reduce((sum, num) => sum + num, 0);

      if (N === k)
         return numSum

      let minWindow = numSum;
      let window = 0;
      const windowSize = N - k
      let left = 0;

      if (windowSize === 0)
         return total


      for (let right = 0; right < N; right++) {
         window += points[right];

         if (right - left + 1 < windowSize)
            continue

         minWindow = Math.min(minWindow, window);
         window -= points[left];
         left++;
      }
      return numSum - minWindow
   };
}


const maxScore = new Solution().maxScore;
console.log(new Solution().maxScore([1, 2], 2) === 3)
console.log(new Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) === 12)
console.log(new Solution().maxScore([2, 2, 2], 2) === 4)
console.log(new Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) === 55)
