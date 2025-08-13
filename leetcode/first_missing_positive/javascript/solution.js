class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: negative marking
    * @param {number[]} numbers
    * @return {number}
    */
   firstMissingPositive(numbers) {
      for (let index = 0; index < numbers.length; index++) {
         if (numbers[index] < 0) {
            numbers[index] = 0;
         }
      }
      for (let index = 0; index < numbers.length; index++) {
         const number = Math.abs(numbers[index]);
         if (
            number > 0 &&
            number <= numbers.length
         ) {
            if (numbers[number - 1] === 0) {
               numbers[number - 1] = -(numbers.length + 1);
            } else if (numbers[number - 1] > 0) {
               numbers[number - 1] = -numbers[number - 1]
            }
         }
      }
      for (let index = 0; index < numbers.length; index++) {
         if (numbers[index] >= 0) {
            return index + 1
         }
      }
      return numbers.length + 1
   };
}
const firstMissingPositive = new Solution().firstMissingPositive;


console.log(new Solution().firstMissingPositive([1, 2, 0]) === 3)
console.log(new Solution().firstMissingPositive([3, 4, -1, 1]) === 2)
console.log(new Solution().firstMissingPositive([7, 8, 9, 11, 12]) === 1)