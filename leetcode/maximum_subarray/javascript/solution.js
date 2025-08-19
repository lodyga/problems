class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      let largestSum = numbers[0];
      let prevMax = 0;

      for (const number of numbers) {
         const currentMax = Math.max(prevMax + number, number);
         prevMax = currentMax;
         largestSum = Math.max(largestSum, currentMax);
      }
      return largestSum
   };
}


class Solution5 {
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


class Solution3 {
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