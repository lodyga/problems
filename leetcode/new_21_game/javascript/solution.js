class Solution {
   /**
    * Time complexity: O(n2)
    *     O(max_pts * draw_point_limit)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number} upper_point_bound
    * @param {number} draw_point_limit
    * @param {number} maxPts
    * @return {number}
    */
   new21Game(upper_point_bound, draw_point_limit, maxPts) {
      const memo = Array(draw_point_limit + 1).fill(-1);

      const dfs = (score) => {
         if (score >= draw_point_limit) {
            return score <= upper_point_bound ? 1 : 0
         }
         else if (memo[score] !== -1) {
            return memo[score]
         }

         let points = 0;
         for (let point = 1; point <= maxPts; point++) {
            points += dfs(score + point);
         }
         memo[score] = points / maxPts;
         return memo[score]
      }
      return dfs(0)
   };
}


const new21Game = new Solution().new21Game;
console.log(new Solution().new21Game(10, 1, 10).toFixed(5) === (1).toFixed(5))
console.log(new Solution().new21Game(6, 1, 10).toFixed(5) === (0.6).toFixed(5))
console.log(new Solution().new21Game(2, 2, 10).toFixed(5) === (0.11).toFixed(5))
console.log(new Solution().new21Game(3, 2, 3).toFixed(5) === (0.88889).toFixed(5))
console.log(new Solution().new21Game(21, 17, 10).toFixed(5) === (0.73278).toFixed(5))
console.log(new Solution().new21Game(0, 0, 1).toFixed(5) === (1).toFixed(5))
console.log(new Solution().new21Game(421, 400, 47).toFixed(5) === (0.71188).toFixed(5))
console.log(new Solution().new21Game(9811, 8776, 1096).toFixed(5) === (0.99696).toFixed(5))
