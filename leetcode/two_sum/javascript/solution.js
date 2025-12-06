class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
    */
   twoSum(numbers, target) {
      const numIndex = new Map();
      for (let index = 0; index < numbers.length; index++) {
         const num = numbers[index];
         const complement = target - num;
         if (numIndex.has(complement))
            return [numIndex.get(complement), index]
         else
            numIndex.set(num, index);
      }
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Plain Object
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
   */
   twoSum(numbers, target) {
      const numIndex = {};
      for (let index = 0; index < numbers.length; index++) {
         let num = numbers[index];
         let complement = target - num;
         if (complement in numIndex) {
            return [numIndex[complement], index];
         } else {
            numIndex[num] = index;
         }
      }
      return null
   }
};


const twoSum = new Solution().twoSum;
console.log(new Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
console.log(new Solution().twoSum([3, 2, 4], 6), [1, 2])
console.log(new Solution().twoSum([3, 3], 6), [0, 1])
