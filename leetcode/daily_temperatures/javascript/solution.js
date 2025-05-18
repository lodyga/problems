class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack, monotonic stack
    * monotonically decreasing stack
    * @param {number[]} temperatures
    * @return {number}
    */
   dailyTemperatures(temperatures) {
      const temperatureStack = [];
      const daysToGetWarmer = Array(temperatures.length).fill(0);

      for (let day = 0; day < temperatures.length; day++) {
         const temperature = temperatures[day];

         while (
            temperatureStack.length &&
            temperatureStack[temperatureStack.length - 1][1] < temperature
         ) {
            const [prevDay, _] = temperatureStack.pop();
            daysToGetWarmer[prevDay] = day - prevDay;
         }
         temperatureStack.push([day, temperature]);
      }
      return daysToGetWarmer
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force
    * @param {number[]} temperatures
    * @return {number}
    */
   dailyTemperatures(temps) {
      const daysToGetWarmer = Array(temps.length).fill(0)

      for (let left = 0; left < temps.length - 1; left++) {
         for (let right = left + 1; right < temps.length; right++) {
            if (temps[left] < temps[right]) {
               daysToGetWarmer[left] = right - left;
               break
            }
         }
      }
      return daysToGetWarmer
   };
}


console.log(new Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
console.log(new Solution().dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
console.log(new Solution().dailyTemperatures([30, 60, 90]), [1, 1, 0])