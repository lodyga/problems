import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(1)
    *     O(10**4) -> O(1) 
    * Auxiliary space complexity: O(1)
    * Tags: backtracking, bfs, iteration
    * @param {string[]} deadends
    * @param {string} target
    * @return {number}
    */
   openLock(deadends, target) {
      const visited = new Set(deadends);

      if ('0000' === target)
         return 0
      else if (visited.has('0000'))
         return -1

      const bfs = () => {
         let turns = 0;
         const queue = new Queue(['0000'])

         while (!queue.isEmpty()) {
            const queue_length = queue.size();
            for (let ql = 0; ql < queue_length; ql++) {
               const code = queue.pop();
               if (code === target)
                  return turns

               for (let index = 0; index < 4; index++) {
                  for (let j of [-1, 1]) {
                     const digit = ((Number(code[index]) + j + 10) % 10).toString();
                     const newCode = code.slice(0, index) + digit + code.slice(index + 1,);
                     if (!visited.has(newCode)) {
                        queue.push(newCode);
                        visited.add(newCode);
                     }
                  }
               }
            }
            turns++;
         }
         return false
      }
      const sol = bfs()
      return sol === false ? -1 : sol
   };
}
const openLock = new Solution().openLock;


console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0202') === 6)
console.log(new Solution().openLock(['8888'], '0009') === 1)
console.log(new Solution().openLock(['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888') === -1)
console.log(new Solution().openLock(['0000'], '8888') === -1)
console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0000') === 0)