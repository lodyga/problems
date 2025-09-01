class Solution52 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers
    * @return {number}
    */
   missingNumber(numbers) {
      const numberSet = new Set(numbers);
      for (let number = 0; number <= numbers.length; number++) {
         if (!numberSet.has(number)) {
            return number
         }
      }
   };
}


class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number[]} numbers
    * @return {number}
    */
   missingNumber(numbers) {
      let xor = 0;

      for (let number = 0; number <= numbers.length; number++) {
         xor ^= number;
      }
      for (const number of numbers) {
         xor ^= number
      }
      return xor
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: math
    * @param {number[]} numbers
    * @return {number}
    */
   missingNumber(numbers) {
      // let total = 0;
      // for (let number = 1; number <= numbers.length; number++) {
      //    total += number;
      // }
      const total = parseInt(numbers.length * (numbers.length + 1) / 2)
      const totalWithountMissing = numbers.reduce((total, number) => total + number);
      return total - totalWithountMissing
   };
}
const missingNumber = new Solution().missingNumber;


console.log(new Solution().missingNumber([3, 0, 1]) === 2)
console.log(new Solution().missingNumber([0, 1]) === 2)
console.log(new Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) === 8)