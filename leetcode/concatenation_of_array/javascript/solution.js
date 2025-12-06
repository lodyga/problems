class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} numbers
    * @return {number[]}
    */
   getConcatenation(numbers) {
      const concated = Array(numbers.length * 2).fill(0);

      for (let index = 0; index < numbers.length; index++) {
         concated[index] = numbers[index];
         concated[index + numbers.length] = numbers[index];
      }
      return concated
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: build-in function
    * @param {number[]} numbers
    * @return {number[]}
    */
   getConcatenation(numbers) {
      return [...numbers, ...numbers]
   };
}


const getConcatenation = new Solution().getConcatenation;
console.log(JSON.stringify(new Solution().getConcatenation([1, 2, 1])) === JSON.stringify([1, 2, 1, 1, 2, 1]))
console.log(JSON.stringify(new Solution().getConcatenation([1, 3, 2, 1])) === JSON.stringify([1, 3, 2, 1, 1, 3, 2, 1]))
