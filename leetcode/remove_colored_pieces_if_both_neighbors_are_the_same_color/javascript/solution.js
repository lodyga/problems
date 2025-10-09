class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {string} colors
    * @return {boolean}
    */
   winnerOfGame(colors) {
      const findTriplet = (left, letter) => {
         for (let index = left; index < colors.length - 1; index++) {
            if (
               colors[index - 1] == colors[index] &&
               colors[index + 1] == colors[index] &&
               colors[index] === letter
            ) {
               index++;
               return index
            }
         }
         return 0
      };

      let leftA = 1;
      let leftB = 1;

      while (true) {
         leftA = findTriplet(leftA, 'A')
         if (leftA === 0)
            return false
         leftB = findTriplet(leftB, 'B')
         if (leftB === 0)
            return true
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {string} colors
    * @return {boolean}
    */
   winnerOfGame(colors) {
      let left = 0;
      let counter = 0;
      for (let right = 0; right < colors.length; right++) {
         if (colors[right] !== colors[left]) {
            left = right;
            continue
         }
         if (right - left + 1 < 3)
            continue
         counter += colors[left] == 'A' ? 1 : -1
      }
      return counter > 0
   };
}


const winnerOfGame = new Solution().winnerOfGame;
console.log(new Solution().winnerOfGame("AAABABB") === true)
console.log(new Solution().winnerOfGame("AA") == false)
console.log(new Solution().winnerOfGame("ABBBBBBBAAA") == false)