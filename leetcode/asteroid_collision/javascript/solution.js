class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {number[]} asteroids
    * @return {number[]}
    */
   asteroidCollision(asteroids) {
      const stack = [];

      for (const asteroid of asteroids) {
         let addAsteroid = true;

         while (stack.length &&
            stack[stack.length - 1] > 0 &&
            asteroid < 0
         ) {
            if (stack[stack.length - 1] < Math.abs(asteroid)) {
               stack.pop();
            } else if (stack[stack.length - 1] === Math.abs(asteroid)) {
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


console.log(new Solution().asteroidCollision([5, 10, -5]), [5, 10])
console.log(new Solution().asteroidCollision([8, -8]), [])
console.log(new Solution().asteroidCollision([10, 2, -5]), [10])
console.log(new Solution().asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])
console.log(new Solution().asteroidCollision([1, 2, -5]), [-5])
console.log(new Solution().asteroidCollision([-2, -2, 1, -2]), [-2, -2, -2])
console.log(new Solution().asteroidCollision([-2, -1, 1, -2]), [-2, -1, -2])
console.log(new Solution().asteroidCollision([-2, 2, 1, -2]), [-2])