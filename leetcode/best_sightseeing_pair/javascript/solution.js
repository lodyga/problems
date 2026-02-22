class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxScoreSightseeingPair(nums) {
      let prevMax = 0;
      let res = 0;

      for (const num of nums) {
         res = Math.max(res, prevMax + num);
         prevMax = Math.max(prevMax, num) - 1;
      }

      return res
   };
}


const maxScoreSightseeingPair = new Solution().maxScoreSightseeingPair;
console.log(new Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]) === 11)
console.log(new Solution().maxScoreSightseeingPair([1, 2]) === 2)
