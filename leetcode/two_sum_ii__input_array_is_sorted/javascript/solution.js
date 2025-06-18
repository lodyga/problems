class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
    */
   twoSum(numbers, target) {
      let left = 0;
      let right = numbers.length - 1;

      while (left < right) {
         const currentSum = numbers[left] + numbers[right];

         if (target === currentSum) {
            return [left + 1, right + 1]
         } else if (target < currentSum) {
            right--;
         } else {
            left++;
         }
      }

   };
}
const twoSum = new Solution().twoSum;


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search, tle
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
    */
   twoSum(numbers, target) {
      for (let index = 0; index < numbers.length - 1; index++) {
         const complement = target - numbers[index];
         let left = index + 1;
         let right = numbers.length - 1;
         
         while (left <= right) {
            let middle = (left + right) >> 1;

            if (complement === numbers[middle]) {
               return [index + 1, middle + 1]
            } else if (complement < numbers[middle]) {
               right--;
            } else {
               left++;
            }
         }
      }
   };
}
const twoSum = new Solution().twoSum;


console.log(new Solution().twoSum([2, 7, 11, 15], 9), [1, 2])
console.log(new Solution().twoSum([2, 3, 4], 6), [1, 3])
console.log(new Solution().twoSum([-1, 0], -1), [1, 2])