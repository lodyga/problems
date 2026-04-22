class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: greedy
    * @param {number[]} heights
    * @return {number[]}
    */
   findBuildings(heights) {
      const res = [heights.length - 1];

      for (let idx = heights.length - 2; idx > -1; idx--) {
         const height = heights[idx];

         if (height > heights[res[res.length - 1]]) {
            res.push(idx);
         }
      }

      return res.reverse()
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: iteration
    * @param {number[]} heights
    * @return {number[]}
    */
   findBuildings(heights) {
      const stack = [];

      for (let idx = 0; idx < heights.length; idx++) {
         const height = heights[idx];

         while (stack.length && stack[stack.length - 1][0] <= height) {
            stack.pop();
         }

         stack.push([height, idx]);
      }

      return stack.map(([, idx]) => idx)
   };
}


const findBuildings = new Solution().findBuildings;
console.log(new Solution().findBuildings([4]).toString() === [0].toString())
console.log(new Solution().findBuildings([4, 2, 3, 1]).toString() === [0, 2, 3].toString())
console.log(new Solution().findBuildings([4, 3, 2, 1]).toString() === [0, 1, 2, 3].toString())
console.log(new Solution().findBuildings([1, 3, 2, 4]).toString() === [3].toString())
