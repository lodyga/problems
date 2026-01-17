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
      let flipsA = 0;
      let flipsB = 0;
      let left = 0;

      for (let right = 0; right < N * 2; right++) {
         const digit = text[right % N];
         flipsA += digit === String((right + 1) % 2) ? 1 : 0;
         flipsB += digit === String(right % 2) ? 1 : 0;

         if (right + 1 < N)
            continue

         minFlips = Math.min(minFlips, Math.min(flipsA, flipsB));
         //  early exit when there are no flips
         if (minFlips === 0)
            return 0

         const leftDigit = text[left];
         flipsA -= leftDigit === String((left + 1) % 2) ? 1 : 0;
         flipsB -= leftDigit === String(left % 2) ? 1 : 0;
         left++;
      }
      return minFlips
   };
}


const minFlips = new Solution().minFlips;
console.log(new Solution().minFlips('111000') === 2)
console.log(new Solution().minFlips('010') === 0)
console.log(new Solution().minFlips('1110') === 1)
console.log(new Solution().minFlips('01001001101') === 2)
