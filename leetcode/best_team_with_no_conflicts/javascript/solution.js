class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} scores
    * @param {number[]} ages
    * @return {number}
    */
   bestTeamScore(scores, ages) {
      const stats = scores.map((value, index) => [value, ages[index]])
      stats.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const cache = stats.map(value => value[0]);
      
      for (let right = 1; right < scores.length; right++) {
         const [score, age] = stats[right];
         
         for (let left = 0; left < right; left++) {
            const [prevScore, prevAge] = stats[left];

            if (prevAge <= age) {
               cache[right] = Math.max(cache[right], score + cache[left]);
            }
         }
      }
      return Math.max(...cache)
   };
}
const bestTeamScore = new Solution().bestTeamScore;


console.log(new Solution().bestTeamScore([3, 4], [7, 8]), 7)
console.log(new Solution().bestTeamScore([4, 3], [7, 8]), 4)
console.log(new Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]), 34)
console.log(new Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 5, 4, 3]), 19)
console.log(new Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]), 16)
console.log(new Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]), 6)
console.log(new Solution().bestTeamScore([1, 3, 7, 3, 2, 4, 10, 7, 5], [4, 5, 2, 1, 1, 2, 4, 1, 4]), 29)
console.log(new Solution().bestTeamScore([6, 5, 1, 7, 6, 5, 5, 4, 10, 4], [3, 2, 5, 3, 2, 1, 4, 4, 5, 1]), 43)