class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: monotonic decreasing stack
    *     A: iteration
    * @param {number[]} temperatures
    * @return {number}
    */
   dailyTemperatures(temperatures) {
      // decreasing temperature day stack
      const dayStack = [];
      const waitDays = Array(temperatures.length).fill(0);

      for (let day = 0; day < temperatures.length; day++) {
         const temp = temperatures[day];
         while (
            dayStack.length &&
            temperatures[dayStack[dayStack.length - 1]] < temp
         ) {
            const prevDay = dayStack.pop();
            waitDays[prevDay] = day - prevDay;
         }
         dayStack.push(day);
      }
      return waitDays
   };
}


class Solution2 {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: brute-force
    * @param {number[]} temperatures
    * @return {number}
    */
   dailyTemperatures(temps) {
      const waitDays = Array(temps.length).fill(0)

      for (let left = 0; left < temps.length - 1; left++) {
         for (let right = left + 1; right < temps.length; right++) {
            if (temps[left] < temps[right]) {
               waitDays[left] = right - left;
               break
            }
         }
      }
      return waitDays
   };
}


const dailyTemperatures = new Solution().dailyTemperatures;
console.log(new Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
console.log(new Solution().dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
console.log(new Solution().dailyTemperatures([30, 60, 90]), [1, 1, 0])
