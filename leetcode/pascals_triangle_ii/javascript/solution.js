class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * @param {number} rowIndex
    * @return {number[]}
    */
   getRow(rowIndex) {
      let lastRow = [1];

      for (let row = 0; row < rowIndex; row++) {
         const currentRow = Array(row + 2).fill(1);
         for (let col = 0; col < lastRow.length - 1; col++) {
            currentRow[col + 1] = lastRow[col] + lastRow[col + 1];
         }
         lastRow = currentRow;
      }
      return lastRow
   };
}


console.log(new Solution().getRow(0), [1])
console.log(new Solution().getRow(1), [1, 1])
console.log(new Solution().getRow(2), [1, 2, 1])
console.log(new Solution().getRow(3), [1, 3, 3, 1])