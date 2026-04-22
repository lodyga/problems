class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    *     A: greedy
    * @param {string} dominoes
    * @return {string}
    */
   pushDominoes(dominoes) {
      const stack = [];
      let rIdx = 0;

      for (const domino of dominoes) {

         if (domino == 'R') {
            stack.push([domino, 0]);
            rIdx = 1;
         }

         else if (domino == 'L') {
            rIdx = 0;
            let idx = 0;

            while (
               stack.length &&
               stack[stack.length - 1][0] == '.' &&
               stack[stack.length - 1][1] > idx
            ) {
               stack.pop();
               idx++;
            }

            while (
               stack.length &&
               stack[stack.length - 1][0] == 'R' &&
               stack[stack.length - 1][1] > idx
            ) {
               if (stack[stack.length - 1][1] == idx + 1) {
                  stack.pop()
                  stack.push(['.', -1])
                  break
               }
               stack.pop();
               idx++
            }

            for (let i = 0; i < idx + 1; i++) {
               stack.push(['L', -1]);
            }

         } else if (domino == '.') {

            if (rIdx) {
               stack.push(['R', rIdx]);
               rIdx++;
            } else {
               stack.push(['.', dominoes.length]);
            }
         }
      }

      return stack.map(([direction,]) => direction).join('')
   };
}


const pushDominoes = new Solution().pushDominoes;
console.log(new Solution().pushDominoes('RR.L') === 'RR.L')
console.log(new Solution().pushDominoes('.L.R...LR..L..') === 'LL.RR.LLRRLL..')
