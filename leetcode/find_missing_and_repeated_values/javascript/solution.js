class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[][]} grid
    * @return {number[]}
    */
   findMissingAndRepeatedValues(grid) {
      const uniqueNumbers = new Set();
      const len = grid.length;
      let repeated;
      let missing;

      for (let row = 0; row < len; row++) {
         for (let col = 0; col < len; col++) {
            const number = grid[row][col];
            if (uniqueNumbers.has(number)) {
               repeated = number;
            }
            uniqueNumbers.add(number);
         }
      }

      for (let number = 1; number < len * len + 1; number++) {
         if (!uniqueNumbers.has(number)) {
            missing = number;
         }
      }
      return [repeated, missing]
   };
}
const findMissingAndRepeatedValues = new Solution().findMissingAndRepeatedValues;


console.log(new Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]), [2, 4])
console.log(new Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]), [9, 5])