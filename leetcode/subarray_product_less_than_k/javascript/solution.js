class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {number[]} numbers
    * @param {number} k
    * @return {number}
    */
   numSubarrayProductLessThanK(numbers, k) {
      let left = 0;
      let windowProduct = 1;
      let subarrayCounter = 0;

      for (let right = 0; right < numbers.length; right++) {
         windowProduct *= numbers[right];

         while (
            left <= right &&
            windowProduct >= k
         ) {
            windowProduct /= numbers[left];
            left++;
         }
         subarrayCounter += (right - left + 1);
      }
      return subarrayCounter
   };
}


console.log(new Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)
console.log(new Solution().numSubarrayProductLessThanK([1, 2, 3], 0), 0)
console.log(new Solution().numSubarrayProductLessThanK([1, 1, 1], 1), 0)
console.log(new Solution().numSubarrayProductLessThanK([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18), 1)