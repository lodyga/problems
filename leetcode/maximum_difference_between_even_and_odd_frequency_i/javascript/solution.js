class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {text}
    * @return {number}
    */
   maxDifference(text) {
      const freqs = Array(26).fill(0);

      for (let index = 0; index < text.length; index++) {
         const letterInd = text.charCodeAt(index) - 'a'.charCodeAt(0)
         freqs[letterInd]++;
      }
      
      let maxOddFreq = 1;
      let minEvenFreq = text.length;
      for (const freq of freqs) {
         if (freq % 2) {
            maxOddFreq = Math.max(maxOddFreq, freq);
         } else if (freq) {
            minEvenFreq = Math.min(minEvenFreq, freq);
         }
      }

      return maxOddFreq - minEvenFreq
   };
}


const maxDifference = new Solution().maxDifference;
console.log(new Solution().maxDifference('aaaaabbc') === 3)
console.log(new Solution().maxDifference('abcabcab') === 1)
console.log(new Solution().maxDifference('yzyyys') === -3)
console.log(new Solution().maxDifference('sssgssiisisiggigsigiiigigggigiggsigggggigsigsisgsgiissisgsiggigssgsgisiisgsgggiigiiggiii') === -3)
