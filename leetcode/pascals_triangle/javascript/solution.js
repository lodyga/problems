class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: list
    *     A: bottom-up
    * @param {number} ROW_COUNT
    * @return {number[][]}
    */
   generate(rowCount) {
      const triangle = [];

      for (let index = 1; index <= rowCount; index++) {
         const row = Array(index).fill(1);

         for (let col = 0; col < index - 2; col++) {
            row[col + 1] = (
               triangle[triangle.length - 1][col] + 
               triangle[triangle.length - 1][col + 1]
            );
         }
         triangle.push(row);
      }
      return triangle
   };
}


const generate = new Solution().generate;
console.log(JSON.stringify(new Solution().generate(1)) === JSON.stringify([[1]]))
console.log(JSON.stringify(new Solution().generate(2)) === JSON.stringify([[1], [1, 1]]))
console.log(JSON.stringify(new Solution().generate(5)) === JSON.stringify([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]))
