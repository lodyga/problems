class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: prefix sum
    * @param {number[]} numbers
    * @return {number}
    */
   pivotIndex(numbers) {
      let prefixSum = 0;
      let postfixSum = numbers.reduce((sum, number) => sum + number, 0);

      for (let index = 0; index < numbers.length; index++) {
         postfixSum -= numbers[index];
         prefixSum += index ? numbers[index - 1] : 0

         if (prefixSum === postfixSum)
            return index
      }
      return -1
   };
}
const pivotIndex = new Solution().pivotIndex;


console.log(new Solution().pivotIndex([1, 7, 3, 6, 5, 6]), 3)
console.log(new Solution().pivotIndex([1, 2, 3]), -1)
console.log(new Solution().pivotIndex([2, 1, -1]), 0)