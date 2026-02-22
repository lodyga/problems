class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, greedy, sorting
    * @param {number[][]} pairs
    * @return {number}
    */
   findLongestChain(pairs) {
      pairs.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      let counter = 0;
      let prevEnd = pairs[0][0] - 1;

      for (const [start, end] of pairs) {
         if (prevEnd < start) {
            counter += 1;
            prevEnd = end;
         }
         prevEnd = Math.min(prevEnd, end)
      }
      return counter
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, greedy, sorting
    * @param {number[][]} pairs
    * @return {number}
    */
   findLongestChain(pairs) {
      pairs.sort((a, b) => a[1] - b[1]);
      let counter = 0;
      let prevEnd = pairs[0][0] - 1;

      for (const [start, end] of pairs) {
         if (prevEnd < start) {
            counter += 1;
            prevEnd = end;
         }
      }
      return counter
   };
}


const findLongestChain = new Solution().findLongestChain;
console.log(new Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]) === 2);
console.log(new Solution().findLongestChain([[1, 2], [7, 8], [4, 5]]) === 3);
