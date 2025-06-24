class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} days
    * @param {number[]} costs
    * @return {number}
    */
   mincostTickets(days, costs) {
      const memo = new Map();  // {day_index: min cost} minimum cost to travel from day dayIndex pointing day onwards
      const validities = [1, 7, 30];
      return dfs(0)

      function dfs(dayIndex) {
         if (dayIndex >= days.length) {
            return 0
         } else if (memo.has(dayIndex)) {
            return memo.get(dayIndex)
         }

         let minCost = Infinity;

         for (let i = 0; i < 3; i++) {
            const cost = costs[i];
            const validity = validities[i];
            let dayIndexDelta = 1;
            
            while (
               dayIndex + dayIndexDelta < days.length &&
               days[dayIndex + dayIndexDelta] < days[dayIndex] + validity
            ) {
               dayIndexDelta++;
            }
            minCost = Math.min(minCost, cost + dfs(dayIndex + dayIndexDelta));
         }
         
         memo.set(dayIndex, minCost)
         return minCost
      }
   };
}


console.log(new Solution().mincostTickets([5], [2, 7, 15]) === 2)
console.log(new Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) === 11)
console.log(new Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) === 17)
console.log(new Solution().mincostTickets([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]) === 423)