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
      let prevColor = -1;
      let maxTime = 0;
      let cost = 0;

      for (let index = 0; index < colors.length; index++) {
         const color = colors[index];
         const time = neededTime[index];

         if (color === prevColor) {
            cost += Math.min(maxTime, time);
            maxTime = Math.max(maxTime, time);
         } else {
            prevColor = color;
            maxTime = time;
         }
      }
      return cost
   };
}


const minCost = new Solution().minCost;
console.log(new Solution().minCost('abaac', [1, 2, 3, 4, 5]) === 3)
console.log(new Solution().minCost('abc', [1, 2, 3]) === 0)
console.log(new Solution().minCost('aabaa', [1, 2, 3, 4, 1]) === 2)
console.log(new Solution().minCost('bbbaaa', [4, 9, 3, 8, 8, 9]) === 23)
