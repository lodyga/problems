import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap, string
    *     A: greedy, iteration
    * @param {number} a
    * @param {number} b
    * @param {number} c
    * @return {string}
    */
   longestDiverseString(a, b, c) {
      const letterHeap = new MaxPriorityQueue(x => x[0]);
      let res = [];
      let prevLetter = '';
      let prevFreq = 0;

      for (const [letter, freq] of [['a', a], ['b', b], ['c', c]]) {
         if (freq) {
            letterHeap.push([freq, letter]);
         }
      }

      while (!letterHeap.isEmpty()) {
         const [freq, letter] = letterHeap.pop();

         if (prevFreq) {
            letterHeap.push([prevFreq, prevLetter]);
         }

         // Limit current letter frequency because of previous letter with higher frequency.
         const k = (freq === 1 || freq < prevFreq) ? 1 : 2;

         res.push(letter.repeat(k));
         prevFreq = freq - k;
         prevLetter = letter;
      }

      return res.join('');
   }
}


const longestDiverseString = new Solution().longestDiverseString;
console.log(new Solution().longestDiverseString(1, 1, 7) === "ccaccbcc")
console.log(new Solution().longestDiverseString(7, 1, 0) === "aabaa")
console.log(new Solution().longestDiverseString(6, 1, 1) === "aacaabaa")
console.log(new Solution().longestDiverseString(6, 2, 0) === "aabaabaa")
