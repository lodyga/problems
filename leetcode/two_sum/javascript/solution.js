class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Map
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
    */
   twoSum(numbers, target) {
      const seenNumbers = new Map();
      for (let index = 0; index < numbers.length; index++) {
         const number = numbers[index];
         const complement = target - number;
         if (seenNumbers.has(complement)) {
            return [seenNumbers.get(complement), index]
         } else {
            seenNumbers.set(number, index);
         }
      }
      return null
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Plain Object
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
   */
   // Using Plain Object:
   twoSum(numbers, target) {
      const seenNumbers = {};
      for (let index = 0; index < numbers.length; index++) {
         let number = numbers[index];
         let complement = target - number;
         if (complement in seenNumbers) {
            return [seenNumbers[complement], index];
         } else {
            seenNumbers[number] = index;
         }
      }
      return null
   }
}


console.log(new Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
console.log(new Solution().twoSum([3, 2, 4], 6), [1, 2])
console.log(new Solution().twoSum([3, 3], 6), [0, 1])
console.log(new Solution().twoSum([3, 3], 7), null)
