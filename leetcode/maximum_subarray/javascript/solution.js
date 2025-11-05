class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      let total = 0;
      let maxSum = numbers[0];

      for (const number of numbers) {
         total > 0 ? total += number : total = number
         // total = Math.max(total + number, number);
         maxSum = Math.max(maxSum, total);
      }
      return maxSum
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * Kadane's Algorithm, mutate imput list
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      for (let index = 1; index < numbers.length; index++) {
         numbers[index] += Math.max(numbers[index - 1], 0)
      }
      return Math.max(...numbers)
   };
}


const maxSubArray = new Solution().maxSubArray;
console.log(new Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6)
console.log(new Solution().maxSubArray([1]) === 1)
console.log(new Solution().maxSubArray([5, 4, -1, 7, 8]) === 23)
console.log(new Solution().maxSubArray([-4, -2, -1, -3]) === -1)