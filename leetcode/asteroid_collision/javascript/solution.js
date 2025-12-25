class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *    DS: stack
    *    A: iteration
    * @param {number[]} asteroids
    * @return {number[]}
    */
   asteroidCollision(asteroids) {
      const stack = [];

      for (const asteroid of asteroids) {
         let addAsteroid = true;

         while (
            stack.length &&
            stack[stack.length - 1] >= 0 &&
            asteroid < 0
         ) {
            if (stack[stack.length - 1] < Math.abs(asteroid)) {
               stack.pop();
            } else if (stack[stack.length - 1] + asteroid === 0) {
               stack.pop();
               addAsteroid = false;
               break
            } else {
               addAsteroid = false;
               break
            }
         }
         if (addAsteroid)
            stack.push(asteroid);
      }
      return stack
   };
}


const asteroidCollision = new Solution().asteroidCollision;
console.log(JSON.stringify(new Solution().asteroidCollision([5, 10, -5])) === JSON.stringify([5, 10]))
console.log(JSON.stringify(new Solution().asteroidCollision([8, -8])) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().asteroidCollision([10, 2, -5])) === JSON.stringify([10]))
console.log(JSON.stringify(new Solution().asteroidCollision([-2, -1, 1, 2])) === JSON.stringify([-2, -1, 1, 2]))
console.log(JSON.stringify(new Solution().asteroidCollision([1, 2, -5])) === JSON.stringify([-5]))
console.log(JSON.stringify(new Solution().asteroidCollision([-2, -2, 1, -2])) === JSON.stringify([-2, -2, -2]))
console.log(JSON.stringify(new Solution().asteroidCollision([-2, -1, 1, -2])) === JSON.stringify([-2, -1, -2]))
console.log(JSON.stringify(new Solution().asteroidCollision([-2, 2, 1, -2])) === JSON.stringify([-2]))
