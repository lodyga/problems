class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: heap
    * @param {number} a
    * @param {number} b
    * @param {number} c
    * @return {string}
    */
   longestDiverseString(a, b, c) {
      const abcHeap = new MaxPriorityQueue(x => x[0]);
      let happyString = '';

      for (const [frequency, letter] of [[a, 'a'], [b, 'b'], [c, 'c']]) {
         if (frequency) {
            abcHeap.enqueue([frequency, letter]);
         }
      }

      let prev = [0, ''];
      while (!abcHeap.isEmpty()) {
         let [frequency, letter] = abcHeap.dequeue();
         if (prev[0]) {
            abcHeap.enqueue(prev);
         }
         if (
            frequency === 1 ||
            frequency < prev[0]
         ) {
            happyString += letter;
            frequency--;
         } else {
            happyString += letter + letter;
            frequency -= 2;
         }
         prev = frequency ? [frequency, letter] : [0, ''];
      }
      return happyString
   };
}
const longestDiverseString = new Solution().longestDiverseString;


console.log(new Solution().longestDiverseString(1, 1, 7) === "ccaccbcc")
console.log(new Solution().longestDiverseString(7, 1, 0) === "aabaa")
console.log(new Solution().longestDiverseString(6, 1, 1) === "aacaabaa")
console.log(new Solution().longestDiverseString(6, 2, 0) === "aabaabaa")