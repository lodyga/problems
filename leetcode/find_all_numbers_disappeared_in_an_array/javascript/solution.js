class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {number[]} numbers
    * @return {number[]}
    */
   findDisappearedNumbers(numbers) {
      const numberSet = new Set(numbers);
      const complement = [];

      for (let number = 1; number <= numbers.length; number++) {
         if (!numberSet.has(number)) {
            complement.push(number)
         }
      }
      return complement
   };
}
const findDisappearedNumbers = new Solution().findDisappearedNumbers;


console.log(new Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
console.log(new Solution().findDisappearedNumbers([1, 1]), [2])