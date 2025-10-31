class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation, negative marking
    * @param {number[]} numbers
    * @return {number[]}
    */
   findErrorNums(numbers) {
      let duplicate;
      for (let number of numbers) {
         number = Math.abs(number);
         if (numbers[number - 1] < 0) {
            duplicate = number;
            break
         } else
            numbers[number - 1] *= - 1;
      }

      let xor = 0;
      for (let index = 0; index < numbers.length; index++) {
         const number = numbers[index];
         xor ^= Math.abs(number) ^ (index + 1);
      }
      const missing = xor ^ duplicate;

      return [duplicate, missing]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {number[]} numbers
    * @return {number[]}
    */
   findErrorNums(numbers) {
      const numberFrequency = new Map(numbers.map((_, index) => [index + 1, 0]));

      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
      }
      let duplicate;
      let missing;
      for (const [number, frequency] of numberFrequency.entries()) {
         if (frequency === 0)
            missing = number
         else if (frequency === 2)
            duplicate = number
      }
      return [duplicate, missing]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers
    * @return {number[]}
    */
   findErrorNums(numbers) {
      const numberSet = new Set();
      let duplicate;
      for (const number of numbers) {
         if (numberSet.has(number))
            duplicate = number;
         else
            numberSet.add(number);
      }

      let missing;
      for (let number = 1; number <= numbers.length; number++) {
         if (!numberSet.has(number)) {
            missing = number
            break
         }
      }

      return [duplicate, missing]
   };
}


const findErrorNums = new Solution().findErrorNums;
console.log(new Solution().findErrorNums([1, 2, 2, 4]), [2, 3])
console.log(new Solution().findErrorNums([1, 1]), [1, 2])
console.log(new Solution().findErrorNums([2, 2]), [2, 1])
console.log(new Solution().findErrorNums([2, 3, 2]), [2, 1])