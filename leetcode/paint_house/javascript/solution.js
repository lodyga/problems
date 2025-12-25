class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: bottom-up
    * @param {number[]} houses
    * @return {number}
    */
   minCost(houses) {
      const cache = houses[0];

      for (let index = 1; index < houses.length; index++) {
         const house = houses[index];
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


const minCost = new Solution().minCost;
console.log(new Solution().minCost([[1, 2, 3]]) === 1)
console.log(new Solution().minCost([[1, 2, 3], [1, 4, 6]]) === 3)
console.log(new Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) === 10)
