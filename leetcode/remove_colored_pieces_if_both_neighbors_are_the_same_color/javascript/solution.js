class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     greedy
    * @param {string} colors
    * @return {boolean}
    */
   winnerOfGame(colors) {
      let counter = 0;

      for (let index = 1; index < colors.length - 1; index++) {
         const color = colors[index];
         if (
            colors[index - 1] == color &&
            color == colors[index + 1]
         )
            color === "A" ? counter++ : counter--;
      }

      return counter > 0
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     two pointers
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
console.log(new Solution().winnerOfGame("AAAABBBB") === false)
