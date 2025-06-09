class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[]} numbers
    * @param {number} k
    * @return {number}
    */
   maxSubarrayLength(numbers, k) {
      const window = new Map();  // {number: frequency}
      let left = 0;
      let subarrayLength = 0;

      for (let right = 0; right < numbers.length; right++) {
         const number = numbers[right];

         window.set(number, (window.get(number) || 0) + 1);

         while (window.get(number) > k) {
            const leftNumber = numbers[left];
            window.set(leftNumber, window.get(leftNumber) - 1);
            if (window.get(leftNumber) === 0)
               window.delete(leftNumber);
            left++;
         }

         subarrayLength = Math.max(
            subarrayLength,
            right - left + 1);
      }
      return subarrayLength
   };
}
const maxSubarrayLength = new Solution().maxSubarrayLength;


console.log(new Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) === 6)
console.log(new Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) === 2)
console.log(new Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) === 4)
console.log(new Solution().maxSubarrayLength([1, 1, 2], 2) === 3)
console.log(new Solution().maxSubarrayLength([1, 4, 4, 3], 1) === 2)