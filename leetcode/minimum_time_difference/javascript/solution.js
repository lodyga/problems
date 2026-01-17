class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {string[]} timePoints
    * @return {number}
    */
   findMinDifference(timePoints) {
      const cycle = 24 * 60;
      const minuteList = Array(timePoints.length).fill(cycle);

      for (let index = 0; index < timePoints.length; index++) {
         const timePoint = timePoints[index];
         const minutes = Math.floor(timePoint.slice(3,));
         const hours = Math.floor(timePoint.slice(0, 2));
         minuteList[index] = minutes + hours * 60;
      }

      minuteList.sort((a, b) => a - b);
      minuteList.push(minuteList[0] + cycle);

      let minDiff = cycle;
      for (let index = 0; index < minuteList.length - 1; index++) {
         minDiff = Math.min(minDiff, minuteList[index + 1] - minuteList[index])
         if (minDiff === 0)
            break
      }
      return minDiff
   };
}


const findMinDifference = new Solution().findMinDifference;
console.log(new Solution().findMinDifference(['23:59', '00:00']) === 1)
console.log(new Solution().findMinDifference(['00:00', '23:59', '00:00']) === 0)
console.log(new Solution().findMinDifference(['02:39', '10:26', '21:43']) === 296)
console.log(new Solution().findMinDifference(['00:01', '01:59']) === 118)