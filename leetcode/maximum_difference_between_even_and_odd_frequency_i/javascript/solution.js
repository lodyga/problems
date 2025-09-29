class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {text}
    * @return {number}
    */
   maxDifference(text) {
      const getIndex = (letter) => letter.charCodeAt(0) - 'a'.charCodeAt(0);

      const frequencies = Array(26).fill(0);
      for (const letter of text) {
         frequencies[getIndex(letter)] += 1;
      }
      
      let maxOddFrequency = 0;
      let minEvenFrequency = text.length;
      for (const frequency of frequencies) {
         if (!frequency)
            continue
         if (frequency & 1) {
            maxOddFrequency = Math.max(maxOddFrequency, frequency)
         } else {
            minEvenFrequency = Math.min(minEvenFrequency, frequency)
         }
      }
      return maxOddFrequency - minEvenFrequency
   };
}


const maxDifference = new Solution().maxDifference;
console.log(new Solution().maxDifference('aaaaabbc') === 3)
console.log(new Solution().maxDifference('abcabcab') === 1)
console.log(new Solution().maxDifference('yzyyys') === -3)