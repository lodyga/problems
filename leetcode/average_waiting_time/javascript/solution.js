class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: intervals
    * @param {number[]} customers
    * @return {number}
    */
   averageWaitingTime(customers) {
      let prevEnd = customers[0][0]
      let totalWait = 0;

      for (const [start, prepare] of customers) {
         const end = Math.max(prevEnd, start) + prepare;
         totalWait += end - start;
         prevEnd = end;
      }

      return totalWait / customers.length
   };
}


const averageWaitingTime = new Solution().averageWaitingTime;
console.log(new Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]) === 5)
console.log(new Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) === 3.25)
