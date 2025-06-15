class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} houses
    * @return {number}
    */
   minCost(houses) {
      const cache = houses[0];

      for (const house of houses.slice(1,)) {
         [cache[0], cache[1], cache[2]] =
            [
               house[0] + Math.min(cache[1], cache[2]),
               house[1] + Math.min(cache[0], cache[2]),
               house[2] + Math.min(cache[0], cache[1])
            ]
      }
      return Math.min(...cache)
   };
}


console.log(new Solution().minCost([[1, 2, 3]]) === 1)
console.log(new Solution().minCost([[1, 2, 3], [1, 4, 6]]) === 3)
console.log(new Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) === 10)