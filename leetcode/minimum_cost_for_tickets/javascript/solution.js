class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} days
    * @param {number[]} costs
    * @return {number}
    */
   mincostTickets(days, costs) {
      const UPPER_BOUND = 365000;
      const VALIDS = [1, 7, 30];
      const N = days.length;
      const memo = Array(N + 1).fill(-1);
      memo[N] = 0;

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx];
         }

         let res = UPPER_BOUND;
         let nextIdx = idx;

         for (let i = 0; i < 3; i++) {
            const cost = costs[i];
            const valid = VALIDS[i];

            while (
               nextIdx < N
               && days[nextIdx] < days[idx] + valid
            ) {
               nextIdx++;
            }

            res = Math.min(res, cost + dfs(nextIdx));
         }

         memo[idx] = res
         return res;
      };

      return dfs(0);
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} days
    * @param {number[]} costs
    * @return {number}
    */
   mincostTickets(days, costs) {
      const UPPER_BOUND = 365000;
      const VALIDS = [1, 7, 30];
      const N = days.length;
      const cache = Array(N + 1).fill(UPPER_BOUND);
      cache[N] = 0;



      for (let idx = N - 1; idx > - 1; idx--) {
         let nextIdx = idx;

         for (let i = 0; i < 3; i++) {
            const cost = costs[i];
            const valid = VALIDS[i];

            while (
               nextIdx < N
               && days[nextIdx] < days[idx] + valid
            ) {
               nextIdx++;
            }

            cache[idx] = Math.min(cache[idx], cost + cache[nextIdx]);
         }

      }

      return cache[0];
   };
}


const mincostTickets = new Solution().mincostTickets;
console.log(new Solution().mincostTickets([5], [2, 7, 15]) === 2)
console.log(new Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) === 11)
console.log(new Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) === 17)
console.log(new Solution().mincostTickets([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]) === 423)
