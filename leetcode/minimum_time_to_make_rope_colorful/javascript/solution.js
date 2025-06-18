class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: stack
    * @param {string} colors
    * @param {number[]} neededTime
    * @return {number}
    */
   minCost(colors, neededTime) {
      let timeTotal = 0;
      let stack = null;  // [color, needed time]

      for (let index = 0; index < colors.length; index++) {
         const color = colors[index];
         const time = neededTime[index];

         if (
            stack &&
            stack[0] === color
         ) {
            if (stack[1] >= time) {
               timeTotal += time;
               continue
            } else {
               timeTotal += stack[1];
            }
         }
         stack = [color, time];
      }
      return timeTotal
   };
}
const minCost = new Solution().minCost;


console.log(new Solution().minCost('abaac', [1, 2, 3, 4, 5]) === 3)
console.log(new Solution().minCost('abc', [1, 2, 3]) === 0)
console.log(new Solution().minCost('aabaa', [1, 2, 3, 4, 1]) === 2)