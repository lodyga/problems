class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(k)
    * Tags: sliding window
    * @param {number[]} numbers
    * @param {number} k
    * @return {number}
    */
   maximumSubarraySum(numbers, k) {
      let left = 0
      const windowMap = new Map();
      let windowSum = 0;
      let maxWindow = 0;

      for (let right = 0; right < numbers.length; right++) {
         const number = numbers[right];
         windowMap.set(number, (windowMap.get(number) || 0) + 1);
         windowSum += number;

         if (right - left + 1 < k)
            continue

         if (windowMap.size === k)
            maxWindow = Math.max(maxWindow, windowSum);

         const leftNumber = numbers[left];
         windowMap.set(leftNumber, windowMap.get(leftNumber) - 1);
         if (windowMap.get(leftNumber) === 0)
            windowMap.delete(leftNumber)
         windowSum -= leftNumber;
         left += 1;
      }
      return maxWindow
   }
}


const maximumSubarraySum = new Solution().maximumSubarraySum;
console.log(new Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) === 15)
console.log(new Solution().maximumSubarraySum([4, 4, 4], 3) === 0)
console.log(new Solution().maximumSubarraySum([9, 9, 9, 1, 2, 3], 3) === 12)
console.lgo(new Solution().maximumSubarraySum([1, 5, 4, 2, 4, 1, 3], 4) === 12)