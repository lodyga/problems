class Solution {
   /**
    * Time complexity: O(n^2)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {string[]} numbers
    * @return {string}
    */
   findDifferentBinaryString(numbers) {
      const number = [];
      const numberSet = new Set(numbers);
      return dfs(0)

      function dfs(index) {
         if (number.length === numbers[0].length){
            const fullNumber = number.join('')
            if (numberSet.has(fullNumber)) {
               return false
            } else {
               return fullNumber
            }
         }

         for (const digit of ['0', '1']) {
            number.push(digit);
            const fullNumber = dfs(index + 1);
            if (fullNumber) {
               return fullNumber
            }
            number.pop();
         }
      }
   };
}
const findDifferentBinaryString = new Solution().findDifferentBinaryString;


console.log(new Solution().findDifferentBinaryString(['0']), '1')
console.log(new Solution().findDifferentBinaryString(['01', '10']), '00')
console.log(new Solution().findDifferentBinaryString(['00', '01']), '10')
console.log(new Solution().findDifferentBinaryString(['111', '011', '001']), '000')