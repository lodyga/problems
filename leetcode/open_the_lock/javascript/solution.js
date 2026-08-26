import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(1)
    *     O(10**4) -> O(1) 
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array, tuple, string, hash set
    *     A: bfs, iteration, level-order traversal
    * @param {string[]} deadends
    * @param {string} target
    * @return {number}
    */
   openLock(deadends, target) {
      const visited = new Set(deadends);

      if (visited.has('0000') || visited.has(target)) {
         return -1;
      }

      const queue = new Queue(['0000']);
      let res = 0;

      while (!queue.isEmpty()) {
         const queueSize = queue.size();

         for (let _ = 0; _ < queueSize; _++) {
            const code = queue.pop();
            const chars = code.split('');

            if (code === target) {
               return res;
            }

            for (let idx = 0; idx < 4; idx++) {
               const digit = code[idx].charCodeAt(0) - '0'.charCodeAt(0);

               for (const dx of [-1, 1]) {
                  const newDigit = ((digit + dx) + 10) % 10;
                  chars[idx] = String.fromCharCode(newDigit + '0'.charCodeAt(0));
                  const nextCode = chars.join('');

                  if (!visited.has(nextCode)) {
                     queue.push(nextCode);
                     visited.add(nextCode);
                  }
               }

               chars[idx] = digit;
            }
         }

         res++;
      }

      return -1;
   }
}


const openLock = new Solution().openLock;
console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0202') === 6)
console.log(new Solution().openLock(['8888'], '0009') === 1)
console.log(new Solution().openLock(['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888') === -1)
console.log(new Solution().openLock(['0000'], '8888') === -1)
console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0000') === 0)
