class Solution {
   /**
    * Time complexity: O(n2)
    *     O(maxPts*threshold)
    * Auxiliary space complexity: O(n)
    * Tags: top-down with memoization as hash map
    * @param {number} upper_bound
    * @param {number} threshold
    * @param {number} maxPts
    * @return {number}
    */
   new21Game(upper_bound, threshold, maxPts) {
      const memo = new Map();
      return dfs(0)

      function dfs(score) {
         if (memo.has(score)) {
            return memo.get(score)
         }
         else if (score >= threshold) {
            return score <= upper_bound
         }

         let occurrence = 0;
         for (let points = 1; points <= maxPts; points++) {
            occurrence += dfs(score + points)
         }
         memo.set(score, occurrence / maxPts)
         return memo.get(score)
      }
   };
}
const new21Game = new Solution().new21Game;


console.log(new Solution().new21Game(10, 1, 10), 1)
console.log(new Solution().new21Game(6, 1, 10), 0.6)
console.log(new Solution().new21Game(2, 2, 10), 0.11)
console.log(new Solution().new21Game(3, 2, 3), 0.88889)
console.log(new Solution().new21Game(21, 17, 10), 0.73278)
console.log(new Solution().new21Game(421, 400, 47), 0.71188)  // tle
console.log(new Solution().new21Game(9811, 8776, 1096), 0.99670)  // tle