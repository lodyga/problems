import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: queue
    *     A: bfs, iteration, level-order traversal
    * @param {string} text
    * @param {number} minJump
    * @param {number} maxJump
    * @return {boolean}
    */
   canReach(text, minJump, maxJump) {
      const queue = new Queue([0]);
      let minStart = 0;

      while (queue.size()) {
         const index = queue.pop();
         const start = Math.max(index + minJump, minStart + 1);
         const end = Math.min(index + maxJump, text.length - 1);

         for (let index = start; index <= end; index++) {
            if (text[index] === '0') {
               queue.push(index);
               if (index === text.length - 1)
                  return true
            }
         }
         minStart = end;
      }
      return false
   };
}


const canReach = new Solution().canReach;
console.log(new Solution().canReach('011010', 2, 3) === true)
console.log(new Solution().canReach('01101110', 2, 3) === false)
console.log(new Solution().canReach('01000110110', 2, 3) === true)
console.log(new Solution().canReach('011111000111000001011111010', 6, 8) === true)
