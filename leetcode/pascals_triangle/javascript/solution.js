class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * @param {number} rowCount
    * @return {number[][]}
    */
   generate(rowCount) {
      const triangle = [[1]];

      for (let row = 0; row < rowCount - 1; row++) {
         const lastRow = triangle[triangle.length - 1];
         const newRow = Array(row + 2).fill(1);

         for (let col = 0; col < row; col++) {
            newRow[col + 1] = lastRow[col] + lastRow[col + 1];
         }
         triangle.push(newRow);
      }
      return triangle
   };
}
const generate = new Solution().generate;


console.log(new Solution().generate(1), [[1]])
console.log(new Solution().generate(2), [[1], [1, 1]])
console.log(new Solution().generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])