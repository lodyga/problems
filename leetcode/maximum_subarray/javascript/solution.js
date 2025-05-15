class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      let cache = numbers[0];
      let largestSum = numbers[0];

      for (const number of numbers.slice(1,)) {
         cache = Math.max(number, number + cache);
         largestSum = Math.max(largestSum, cache);
      }
      return largestSum
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      const cache = numbers.slice();

      for (let index = 1; index < numbers.length; index++) {
         cache[index] = Math.max(
            cache[index],
            cache[index] + cache[index - 1]
         );
      }
      return Math.max(...cache)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * mutate imput list
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


console.log(new Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6)
console.log(new Solution().maxSubArray([1]) === 1)
console.log(new Solution().maxSubArray([5, 4, -1, 7, 8]) === 23)
console.log(new Solution().maxSubArray([-4, -2, -1, -3]) === -1)