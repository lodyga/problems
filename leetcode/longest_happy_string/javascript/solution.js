import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap
    *     A: greedy, iteration
    * @param {number} a
    * @param {number} b
    * @param {number} c
    * @return {string}
    */
   longestDiverseString(a, b, c) {
      const letterHeap = new MaxPriorityQueue(x => x[0]);
      let happyList = [];

      for (const [freq, letter] of [[a, 'a'], [b, 'b'], [c, 'c']]) {
         if (freq) {
            letterHeap.enqueue([freq, letter]);
         }
      }

      let prevFreq = 0;
      let prevLetter = '';
      while (letterHeap.size()) {
         const [freq, letter] = letterHeap.dequeue();
         if (prevFreq) {
            letterHeap.enqueue([prevFreq, prevLetter]);
         }
         if (
            freq === 1 ||
            // Limit current letter becouse of letter with highter frequency.
            freq < prevFreq
         ) {
            happyList.push(letter);
            prevFreq = freq - 1;
            prevLetter = letter;
         } else {
            happyList.push(letter);
            happyList.push(letter);
            prevFreq = freq - 2;
            prevLetter = letter;
         }
      }
      return happyList.join('')
   };
}


const longestDiverseString = new Solution().longestDiverseString;
console.log(new Solution().longestDiverseString(1, 1, 7) === "ccaccbcc")
console.log(new Solution().longestDiverseString(7, 1, 0) === "aabaa")
console.log(new Solution().longestDiverseString(6, 1, 1) === "aacaabaa")
console.log(new Solution().longestDiverseString(6, 2, 0) === "aabaabaa")
