class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: prefix sum
    * @param {number[]} numbers
    * @return {number[]}
    */
   productExceptSelf(numbers) {
      const prefix = Array(numbers.length).fill(1);
      for (let index = 0; index < numbers.length - 1; index++) {
         prefix[index + 1] = prefix[index] * numbers[index];
      }

      const postfix = Array(numbers.length).fill(1);
      for (let index = numbers.length - 1; index >= 1; index--) {
         postfix[index - 1] = postfix[index] * numbers[index];
      }

      return prefix.map((value, index) => value * postfix[index])
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: prefix sum
    * @param {number[]} numbers
    * @return {number[]}
    */
   productExceptSelf(numbers) {
      const product = Array(numbers.length).fill(1);
      for (let index = 0; index < numbers.length - 1; index++) {
         product[index + 1] = product[index] * numbers[index];
      }

      let postfix = 1;
      for (let index = numbers.length - 1; index >= 0; index--) {
         product[index] *= postfix;
         postfix *= numbers[index];
      }

      return product
   };
}


console.log(new Solution().productExceptSelf([2, 3, 4, 5]), [60, 40, 30, 24])
console.log(new Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
console.log(new Solution().productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])