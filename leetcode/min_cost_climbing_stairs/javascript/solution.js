class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * mutate input list
    * @param {number[]} cost
    * @return {number}
    */
   minCostClimbingStairs(cost) {
      for (let index = 2; index < cost.length; index++) {
         cost[index] += Math.min(cost[index - 1], cost[index - 2]);
      }
      return Math.min(...cost.slice(-2))
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} cost
    * @return {number}
    */
   minCostClimbingStairs(cost) {
      const cache = [cost[0], cost[1]];

      for (let index = 2; index < cost.length; index++) {
         [cache[0], cache[1]] = [cache[1], cost[index] + Math.min(cache[0], cache[1])];
      }
      return Math.min(...cache)
   };
}


console.log(new Solution().minCostClimbingStairs([10, 15, 20]) === 15)
console.log(new Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) === 6)