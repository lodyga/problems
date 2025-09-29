class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} candies
    * @param {number} childCount
    * @return {number}
    */
   maximumCandies(candies, childCount) {
      const TOTAL = candies.reduce((total, value) => total + value, 0);
      if (childCount > TOTAL)
         return 0

      let left = 1;
      let right = Math.max(...candies);
      let candyPerChild = 0;
      
      while (left <= right) {
         const middle = (left + right) >> 1;
         let happyChildCount = 0;

         for (const candy of candies) {
            if (candy >= middle) {
               happyChildCount += parseInt(candy / middle);
               if (happyChildCount >= childCount)
                  break
            }
         }
         if (happyChildCount >= childCount) {
            left = middle + 1;
            candyPerChild = middle;
         } else {
            right = middle - 1;
         }
      }
      return candyPerChild
   };
}


const maximumCandies = new Solution().maximumCandies;
console.log(new Solution().maximumCandies([5, 8, 6], 3) == 5)
console.log(new Solution().maximumCandies([2, 5], 11) == 0)
console.log(new Solution().maximumCandies([5, 8, 6], 4) == 4)
console.log(new Solution().maximumCandies([5, 8, 6], 5) == 3)
console.log(new Solution().maximumCandies([4, 7, 5], 4) == 3)
console.log(new Solution().maximumCandies([1, 2, 3, 4, 10], 5) == 3)