class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic decreasing stack
    *     A: iteration
    * @param {number[]} temps
    * @return {number}
    */
   dailyTemperatures(temps) {
      // decreasing temperature day stack
      const dayStack = [];
      const res = Array(temps.length).fill(0);

      for (let day = 0; day < temps.length; day++) {
         const temp = temps[day];
         
         while (
            dayStack.length &&
            temps[dayStack[dayStack.length - 1]] < temp
         ) {
            const prevDay = dayStack.pop();
            res[prevDay] = day - prevDay;
         }

         dayStack.push(day);
      }
      return res
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: brute-force
    * @param {number[]} temps
    * @return {number}
    */
   dailyTemperatures(temps) {
      const res = Array(temps.length).fill(0);

      for (let left = 0; left < temps.length - 1; left++) {
         for (let right = left + 1; right < temps.length; right++) {
            if (temps[left] < temps[right]) {
               res[left] = right - left;
               break
            }
         }
      }
      
      return res
   }
}


const dailyTemperatures = new Solution().dailyTemperatures;
console.log(new Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]).toString() === [1, 1, 4, 2, 1, 1, 0, 0].toString())
console.log(new Solution().dailyTemperatures([30, 40, 50, 60]).toString() === [1, 1, 1, 0].toString())
console.log(new Solution().dailyTemperatures([30, 60, 90]).toString() === [1, 1, 0].toString())
