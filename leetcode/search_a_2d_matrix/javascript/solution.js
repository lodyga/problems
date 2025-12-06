class Solution {
   /**
    * Time complexity: O(log(n*m))
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number[][]} matrix
    * @param {number} target
    * @return {boolean}
    */
   searchMatrix(matrix, target) {
      let top = 0;
      let bottom = matrix.length - 1;

      while (top <= bottom) {
         const middleRowIndex = (top + bottom) >> 1;
         const middleRow = matrix[middleRowIndex];

         if (
            target >= middleRow[0] &&
            target <= middleRow[middleRow.length - 1]
         ) {
            let left = 0;
            let right = matrix[0].length - 1;

            while (left <= right) {
               const middle = (left + right) >> 1;
               const middleNum = middleRow[middle];

               if (target === middleNum) {
                  return true
               } else if (target < middleNum) {
                  right = middle - 1;
               } else {
                  left = middle + 1;
               }
            }
            return false

         } else if (target < middleRow[0]) {
            bottom = middleRowIndex - 1;
         } else {
            top = middleRowIndex + 1;
         }
      }

      return false
   };
}


const searchMatrix = new Solution().searchMatrix;
console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) === true)
console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) === false)
