class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting
    * @param {number} target
    * @param {number[]} positions
    * @param {number[]} speeds
    * @return {number}
    */
   carFleet(target, positions, speeds) {
      let prevTime = 0;
      let fleetCounter = 0;
      const cars = positions
         .map((value, index) => [value, speeds[index]])
         .sort((a, b) => b[0] - a[0]);

      for (const [position, speed] of cars) {
         const distance = target - position;
         const time = distance / speed;

         if (time > prevTime) {
            fleetCounter += 1
            prevTime = time
         }
      }
      return fleetCounter
   };
}


const carFleet = new Solution().carFleet;
console.log(new Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) === 3)
console.log(new Solution().carFleet(10, [3], [3]) === 1)
console.log(new Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) === 1)
console.log(new Solution().carFleet(10, [0, 4, 2], [2, 1, 3]) === 1)
