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

      if (visited.has('0000'))
         return -1

      const bfs = () => {
         const queue = new Queue(['0000'])
         let turns = 0;

         while (queue.size()) {
            const queue_size = queue.size();

            for (let qi = 0; qi < queue_size; qi++) {
               const code = queue.pop();
               const chars = code.split('')

               if (code === target)
                  return turns

               for (let index = 0; index < 4; index++) {
                  const digit = code[index].charCodeAt(0) - 48;

                  for (const d of [-1, 1]) {
                     const nei_digit = (digit + d + 10) % 10;
                     chars[index] = String.fromCharCode(48 + nei_digit);
                     const code = chars.join('');

                     if (!visited.has(code)) {
                        queue.push(code);
                        visited.add(code);
                     }
                  }
                  chars[index] = digit;
               }
            }
            turns++;
         }
         return -1
      }
      return bfs()
   };
}


const openLock = new Solution().openLock;
console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0202') === 6)
console.log(new Solution().openLock(['8888'], '0009') === 1)
console.log(new Solution().openLock(['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888') === -1)
console.log(new Solution().openLock(['0000'], '8888') === -1)
console.log(new Solution().openLock(['0201', '0101', '0102', '1212', '2002'], '0000') === 0)
