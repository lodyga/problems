class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} candies
    * @param {number} k
    * @return {number}
    */
   maximumCandies(candies, k) {
      let left = 1;
      let right = Math.min(
         Math.max(...candies),
         Math.floor(candies.reduce((sum, num) => sum + num, 0) / k));
      let res = 0;

      while (left <= right) {
         const mid = Math.floor((left + right) / 2);
         let happy = 0;

         for (const candy of candies) {
            happy += Math.floor(candy / mid);
            if (happy >= k)
               break
         }

         if (happy >= k) {
            left = mid + 1;
            res = mid;
         } else {
            right = mid - 1;
         }
      }
      return res
   };
}


const maximumCandies = new Solution().maximumCandies;
console.log(new Solution().maximumCandies([5, 8, 6], 3) === 5)
console.log(new Solution().maximumCandies([2, 5], 11) === 0)
console.log(new Solution().maximumCandies([5, 8, 6], 4) === 4)
console.log(new Solution().maximumCandies([5, 8, 6], 5) === 3)
console.log(new Solution().maximumCandies([4, 7, 5], 4) === 3)
console.log(new Solution().maximumCandies([1, 2, 3, 4, 10], 5) === 3)
