class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {number[]} cardPoints
    * @param {number} k
    * @return {number}
    */
   maxScore(cardPoints, k) {
      let windowLength = cardPoints.length - k;
      let window = 0;
      let total = cardPoints.reduce((total, value) => total + value, 0);
      let minWindow = total;
      let left = 0;

      if (windowLength === 0)
         return total

      for (let right = 0; right < cardPoints.length; right++) {
         window += cardPoints[right];

         if (right - left + 1 < windowLength)
            continue

         minWindow = Math.min(minWindow, window);
         window -= cardPoints[left];
         left++;
      }
      return total - minWindow
   };
}


const maxScore = new Solution().maxScore;
console.log(new Solution().maxScore([1, 2], 2) === 3)
console.log(new Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) === 12)
console.log(new Solution().maxScore([2, 2, 2], 2) === 4)
console.log(new Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) === 55)