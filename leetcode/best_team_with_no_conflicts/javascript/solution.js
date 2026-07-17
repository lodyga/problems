class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} scores
    * @param {number[]} ages
    * @return {number}
    */
   bestTeamScore(scores, ages) {
      const N = scores.length;
      const data = scores.map((val, idx) => [val, ages[idx]]);
      data.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      // [starting idx + 1: LIS length]
      const memo = Array(N + 1).fill(-1);

      const dfs = (idx, prevIdx) => {
         if (idx === N) {
            return 0;
         }
         else if (memo[prevIdx + 1] !== -1) {
            return memo[prevIdx + 1];
         }

         const [score, age] = data[idx];
         const prevAge = prevIdx === -1 ? -1 : data[prevIdx][1];

         const skip = dfs(idx + 1, prevIdx);
         const take = (age >= prevAge) ? score + dfs(idx + 1, idx) : 0;

         const lis = Math.max(skip, take);
         memo[prevIdx + 1] = lis;
         return lis;
      }

      return dfs(0, -1);
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} scores
    * @param {number[]} ages
    * @return {number}
    */
   bestTeamScore(scores, ages) {
      const N = scores.length;
      const data = scores.map((val, idx) => [val, ages[idx]])
      data.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const cache = data.map(val => val[0]);

      for (let left = N - 1; left > -1; left--) {
         const [score, age] = data[left];

         for (let right = left + 1; right < N; right++) {
            const nextAge = data[right][1];

            if (age <= nextAge) {
               cache[left] = Math.max(
                  cache[left],
                  score + cache[right]
               );
            }
         }
      }

      return Math.max(...cache);
   }
}


const bestTeamScore = new Solution().bestTeamScore;
console.log(new Solution().bestTeamScore([3, 4], [7, 8]) === 7)
console.log(new Solution().bestTeamScore([4, 3], [7, 8]) === 4)
console.log(new Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) === 34)
console.log(new Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 5, 4, 3]) === 19)
console.log(new Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) === 16)
console.log(new Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) === 6)
console.log(new Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]) === 29)
console.log(new Solution().bestTeamScore([6, 5, 1, 7, 6, 5, 5, 4, 10, 4], [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]) === 43)
