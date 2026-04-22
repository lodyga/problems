class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list, array
    *     A: sorting
    * @param {string} word
    * @return {number}
    */
   minimumPushes(word) {
      let pushes = 0;
      const letterFreq = Array(26).fill(0);

      for (const letter of word) {
         const idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         letterFreq[idx] += 1;
      }

      letterFreq.sort((a, b) => b - a);

      for (let idx = 0; idx < letterFreq.length; idx++) {
         const freq = letterFreq[idx];
         if (freq === 0) break
         const pushesInLayer = Math.floor(idx / 8) + 1;
         pushes += letterFreq[idx] * pushesInLayer;
      }

      return pushes
   };
}


const minimumPushes = new Solution().minimumPushes;
console.log(new Solution().minimumPushes("abcde") === 5)
console.log(new Solution().minimumPushes("xyzxyzxyzxyz") === 12)
console.log(new Solution().minimumPushes("aabbccddeeffgghhiiiiii") === 24)
console.log(new Solution().minimumPushes("hiknogatpyjzcdbe") === 24)
