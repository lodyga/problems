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
      const data = scores.map((value, index) => [value, ages[index]])
      data.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0])
      // [starting index + 1: LIS length]
      const memo = Array(data.length + 1).fill(-1);

      const dfs = (index, prevIndex) => {
         if (index === data.length)
            return 0
         else if (memo[prevIndex + 1] !== -1)
            return memo[prevIndex + 1]

         let prevAge = -1
         if (prevIndex !== -1)
            [, prevAge] = data[prevIndex];
         const [score, age] = data[index];

         // skip current score
         const skip = dfs(index + 1, prevIndex);
         // take current score
         let take = 0;
         if (age >= prevAge)
            take = score + dfs(index + 1, index)

         const lis = Math.max(skip, take);
         memo[prevIndex + 1] = lis;
         return lis
      }
      return dfs(0, -1)
   };

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
      const stats = scores.map((value, index) => [value, ages[index]])
      stats.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const cache = stats.map(value => value[0]);

      for (let left = stats.length - 1; left > -1; left--) {
         const [score, age] = stats[left];

         for (let right = left + 1; right < stats.length; right++) {
            const [, nextAge] = stats[right];

            if (age <= nextAge) {
               cache[left] = Math.max(cache[left], score + cache[right]);
            }
         }
      }
      return Math.max(...cache)
   };
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
