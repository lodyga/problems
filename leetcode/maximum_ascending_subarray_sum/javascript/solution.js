class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding windowd
    * @param {number[]} numbers
    * @return {number}
    */
   maxAscendingSum(numbers) {
      let prevNumber = 0;
      let window = 0;
      let maxWindow = 0;

      for (const number of numbers) {
         if (number > prevNumber) {
            window += number;
            maxWindow = Math.max(maxWindow, window);
         } else {
            window = number
         }
         prevNumber = number;
      }
      return maxWindow
   };
}


const maxAscendingSum = new Solution().maxAscendingSum;
console.log(new Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) === 65)
console.log(new Solution().maxAscendingSum([10, 20, 30, 40, 50]) === 150)
console.log(new Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) === 33)