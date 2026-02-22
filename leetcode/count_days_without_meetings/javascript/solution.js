class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: intervals, sorting
    * @param {number} days
    * @param {number[]} meetings
    * @return {number}
    */
   countDays(days, meetings) {
      meetings.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      let counter = 0;
      let prevEnd = 0;

      for (const [start, end] of meetings) {
         counter += Math.max(0, start - prevEnd - 1);
         prevEnd = Math.max(prevEnd, end);
      }
      return counter + Math.max(0, days - prevEnd)
   };
}


const countDays = new Solution().countDays;
console.log(new Solution().countDays(10, [[5, 7], [1, 3], [9, 10]]) === 2)
console.log(new Solution().countDays(5, [[2, 4], [1, 3]]) === 1)
console.log(new Solution().countDays(6, [[1, 6]]) === 0)
console.log(new Solution().countDays(57, [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48], [3, 31]]) === 1)
console.log(new Solution().countDays(14, [[6, 11], [7, 13], [8, 9], [5, 8], [3, 13], [11, 13], [1, 3], [5, 10], [8, 13], [3, 9]]) === 1)
