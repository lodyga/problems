import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: bfs
    * @param {string} number
    * @param {number} minJump
    * @param {number} maxJump
    * @return {boolean}
    */
   canReach(number, minJump, maxJump) {
      const queue = new Queue([0]);
      let farthest = 0;
      
      while (queue.size()) {
         const index = queue.pop();
         const start = Math.max(index + minJump, farthest + 1);
         const end = Math.min(index + maxJump + 1, number.length);

         for (let index = start; index < end; index++) {
            if (number[index] === '0') {
               queue.push(index);
               if (index === number.length - 1) {
                  return true
               }
            }
         }
         farthest = end - 1;
      }
      return false
   };
}
const canReach = new Solution().canReach;


console.log(new Solution().canReach('011010', 2, 3) === true)
console.log(new Solution().canReach('01101110', 2, 3) === false)
console.log(new Solution().canReach('01000110110', 2, 3) === true)