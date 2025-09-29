class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} numbers
    * @return {number}
    */
   longestMonotonicSubarray(numbers) {
      let increasingLen = 1;
      let decreasingLen = 1;
      let maxLen = 1;

      for (let index = 1; index < numbers.length; index++) {
         const prevNumber = numbers[index - 1];
         const number = numbers[index];

         if (prevNumber < number) {
            increasingLen++;
            decreasingLen = 1;
         } else if (prevNumber > number) {
            decreasingLen++;
            increasingLen = 1;
         } else {
            increasingLen = 1;
            decreasingLen = 1;
         }
         maxLen = Math.max(maxLen, increasingLen, decreasingLen);
      }
      return maxLen
   };
}


const longestMonotonicSubarray = new Solution().longestMonotonicSubarray;
console.log(new Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]) === 2)
console.log(new Solution().longestMonotonicSubarray([3, 3, 3, 3]) === 1)
console.log(new Solution().longestMonotonicSubarray([3, 2, 1]) === 3)