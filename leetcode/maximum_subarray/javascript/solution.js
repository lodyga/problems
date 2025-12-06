class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: greedy (Kadane)
    * @param {number[]} numbers
    * @return {number}
    */
   maxSubArray(numbers) {
      let subarraySum = 0;
      let maxSum = numbers[0];

      for (const number of numbers) {
         subarraySum > 0 ? subarraySum += number : subarraySum = number
         // subarraySum = Math.max(subarraySum + number, number);
         maxSum = Math.max(maxSum, subarraySum);
      }
      return maxSum
   };
}


const maxSubArray = new Solution().maxSubArray;
console.log(new Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6)
console.log(new Solution().maxSubArray([1]) === 1)
console.log(new Solution().maxSubArray([5, 4, -1, 7, 8]) === 23)
console.log(new Solution().maxSubArray([-4, -2, -1, -3]) === -1)
