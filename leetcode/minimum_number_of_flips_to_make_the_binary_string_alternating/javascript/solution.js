class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {string} text
    * @return {number}
    */
   minFlips(text) {
      const N = text.length;
      let minFlips = N;
      let left = 0;
      let s1Flips = 0;
      let s2Flips = 0;

      for (let right = 0; right < N * 2; right++) {
         const char = text[right % N];
         s1Flips += char === String((right + 1) % 2) ? 1 : 0;
         s2Flips += char === String(right % 2) ? 1 : 0;

         if (right < N - 1) continue;

         minFlips = Math.min(minFlips, s1Flips, s2Flips);
         if (minFlips === 0) return 0;

         const leftChar = text[left];
         s1Flips -= leftChar === String((left + 1) % 2) ? 1 : 0;
         s2Flips -= leftChar === String(left % 2) ? 1 : 0;
         left++;
      }

      return minFlips;
   }
}


const minFlips = new Solution().minFlips;
console.log(new Solution().minFlips('111000') === 2)
console.log(new Solution().minFlips('010') === 0)
console.log(new Solution().minFlips('1110') === 1)
console.log(new Solution().minFlips('01001001101') === 2)
