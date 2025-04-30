class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} numbers
    * @return {number[]}
    */
   getConcatenation(numbers) {
      const concatenatedArray = Array(numbers.length * 2);

      for (let index = 0; index < numbers.length; index++) {
         concatenatedArray[index] = numbers[index];
         concatenatedArray[index + numbers.length] = numbers[index];
      }
      return concatenatedArray
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} numbers
    * @return {number[]}
    */
   getConcatenation(numbers) {
      return [...numbers, ...numbers]
   };
}


console.log(new Solution().getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])
console.log(new Solution().getConcatenation([1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])