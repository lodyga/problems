class Solution {
   /**
    * Time complexity: O(log(n*m))
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[][]} matrix
    * @param {number} target
    * @return {boolean}
    */
   searchMatrix(matrix, target) {
      let top = 0;
      let bottom = matrix.length - 1;
      let left = 0;
      let right = matrix[0].length - 1;
      let isRowFound = false;
      let middleRow = [];

      while (top <= bottom) {
         const middleRowIndex = (top + bottom) >> 1;
         middleRow = matrix[middleRowIndex];

         if (
            target >= middleRow[0] &&
            target <= middleRow[middleRow.length - 1]
         ) {
            isRowFound = true;
            break
         } else if (target < middleRow[0]) {
            bottom = middleRowIndex - 1
         } else {
            top = middleRowIndex + 1
         }
      }
      // early exit
      if (!isRowFound) {
         return false
      }
      while (left <= right) {
         const middleColIndex = (left + right) >> 1;
         const middleNumber = middleRow[middleColIndex]

         if (target === middleNumber) {
            return true
         } else if (target < middleNumber) {
            right = middleColIndex - 1;
         } else {
            left = middleColIndex + 1;
         }
      }
      return false
   };
}
const searchMatrix = new Solution().searchMatrix;


console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), true)
console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), false)