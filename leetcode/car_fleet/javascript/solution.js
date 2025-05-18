class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {number} target
    * @param {number[]} positions
    * @param {number[]} speeds
    * @return {number}
    */
   carFleet(target, positions, speeds) {
      const fleetStack = [];

      const cars = positions
         .map((position, index) => [position, speeds[index]])
         .sort((a, b) => b[0] - a[0]);
      
      for (const [position, speed] of cars) {
         const timeToFinish = (target - position) / speed;
         if (fleetStack.length && fleetStack[fleetStack.length - 1] >= timeToFinish) 
            continue
         
         fleetStack.push(timeToFinish);
      }
      return fleetStack.length
   };
}


console.log(new Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
console.log(new Solution().carFleet(10, [3], [3]), 1)
console.log(new Solution().carFleet(100, [0, 2, 4], [4, 2, 1]), 1)
console.log(new Solution().carFleet(10, [0, 4, 2], [2, 1, 3]), 1)