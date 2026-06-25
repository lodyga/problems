class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} colors
    * @param {number[]} neededTime
    * @return {number}
    */
   minCost(colors, neededTime) {
      let prevColor = '';
      let prevTime = 0;
      let res = 0;

      for (let idx = 0; idx < colors.length; idx++) {
         const color = colors[idx];
         const time = neededTime[idx];

         if (color === prevColor) {
            res += Math.min(prevTime, time);
            prevTime = Math.max(prevTime, time);
         } 
         else {
            prevColor = color;
            prevTime = time;
         }
      }

      return res;
   }
}


const minCost = new Solution().minCost;
console.log(new Solution().minCost('abaac', [1, 2, 3, 4, 5]) === 3)
console.log(new Solution().minCost('abc', [1, 2, 3]) === 0)
console.log(new Solution().minCost('aabaa', [1, 2, 3, 4, 1]) === 2)
console.log(new Solution().minCost('bbbaaa', [4, 9, 3, 8, 8, 9]) === 23)
