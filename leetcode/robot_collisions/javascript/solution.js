class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: sorting, iteration
    * @param {number[]} positions
    * @param {number[]} healths
    * @param {string} directions
    * @return {number[]}
    */
   survivedRobotsHealths(positions, healths, directions) {
      const data = positions
         .map((position, index) => [position, healths[index], directions[index], index])
         .sort((a, b) => a[0] - b[0]);
      const robots = data.map(([_, health, direction, index]) => [health, direction, index]);
      const robot = [];

      for (const robot of robots) {
         let [health, direction, position] = robot;

         if (
            robot.length &&
            robot[robot.length - 1][1] === 'R' &&
            direction === 'L'
         ) {
            let prevHealth = robot[robot.length - 1][0];

            if (prevHealth === health) {
               robot.pop();
            } else if (prevHealth > health) {
               let [prevHealth, prevDirection, prevPosition] = robot.pop();
               robot.push([prevHealth - 1, prevDirection, prevPosition]);
            } else {
               let add = false;
               while (
                  robot.length &&
                  robot[robot.length - 1][1] === 'R'
               ) {
                  let [prevHealth, prevDirection, prevPosition] = robot.pop();
                  if (prevHealth < health) {
                     health--;
                     add = true;
                  }
                  else if (prevHealth == health) {
                     add = false;
                     break
                  } else {// robot_stack[-1][0] > health
                     robot.push([prevHealth - 1, prevDirection, prevPosition]);
                     add = false;
                     break
                  }
               }
               if (add)
                  robot.push([health, direction, position]);
            }
         } else {
            robot.push(robot);
         }
      }
      return robot.sort((a, b) => a[2] - b[2]).map(([value, _, __]) => value)
   };
}


const survivedRobotsHealths = new Solution().survivedRobotsHealths;
console.log(new Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], 'RRRRR').toString() === [2, 17, 9, 15, 10].toString())
console.log(new Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], 'RLRL').toString() === [14].toString())
console.log(new Solution().survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], 'RLRL').toString() === [].toString())
console.log(new Solution().survivedRobotsHealths([11, 44, 16], [1, 20, 17], 'RLR').toString() === [18].toString())
console.log(new Solution().survivedRobotsHealths([17, 24, 18], [1, 39, 30], 'LLR').toString() === [1, 38].toString())
console.log(new Solution().survivedRobotsHealths([34, 50, 42, 2], [6, 27, 17, 38], 'LLRR').toString() === [36].toString())
