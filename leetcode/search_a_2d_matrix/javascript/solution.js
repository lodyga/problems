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
         const midRowIndex = Math.floor((top + bottom) / 2);
         const midRow = matrix[midRowIndex];

         if (
            target >= midRow[0]
            && target <= midRow[midRow.length - 1]
         ) {
            let left = 0;
            let right = matrix[0].length - 1;

            while (left <= right) {
               const mid = Math.floor((left + right) / 2);
               const midNum = midRow[mid];

               if (target === midNum) {
                  return true;
               } else if (target < midNum) {
                  right = mid - 1;
               } else {
                  left = mid + 1;
               }
            }

            return false;

         } 
         else if (target < midRow[0]) {
            bottom = midRowIndex - 1;
         } 
         else {
            top = midRowIndex + 1;
         }
      }

      return false;
   }
}


const searchMatrix = new Solution().searchMatrix;
console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) === true)
console.log(new Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) === false)
