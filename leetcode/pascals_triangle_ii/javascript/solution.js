class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: 
    *     DS: list
    *     A: bottom-up
    * @param {number} rowIndex
    * @return {number[]}
    */
   getRow(rowIndex) {
      let prevRowVals = [1];

      for (let row = 0; row < rowIndex; row++) {
         const rowVals = [1];
         for (let col = 0; col < row; col++) {
            rowVals.push(prevRowVals[col] + prevRowVals[col + 1]);
         }
         rowVals.push(1);
         prevRowVals = rowVals;
      }
      return prevRowVals
   };
}


const getRow = new Solution().getRow;
console.log(JSON.stringify(new Solution().getRow(0)) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().getRow(1)) === JSON.stringify([1, 1]))
console.log(JSON.stringify(new Solution().getRow(2)) === JSON.stringify([1, 2, 1]))
console.log(JSON.stringify(new Solution().getRow(3)) === JSON.stringify([1, 3, 3, 1]))
