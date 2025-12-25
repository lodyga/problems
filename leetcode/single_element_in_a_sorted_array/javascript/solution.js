class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number[]} nums
    * @return {number}
    */
   singleNonDuplicate(nums) {
      let left = 0
      let right = nums.length - 1

      while (left <= right) {
         const middle = (left + right) >> 1;

         if (
            left === right ||
            (nums[middle - 1] != nums[middle] && nums[middle] != nums[middle + 1])
         )
            return nums[middle]

         if (nums[middle] === nums[middle + 1]) {
            if ((middle - left) % 2 === 1) {
               right = middle - 1;
            } else {
               left = middle + 2;
            }
         } else if (nums[middle - 1] === nums[middle]) {
            if ((middle - left) % 2 === 1) {
               left = middle + 1;
            } else {
               right = middle - 2;
            }
         }
      }
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: bit manipulation
    * @param {number[]} nums
    * @return {number}
    */
   singleNonDuplicate(nums) {
      let xor = 0;
      for (const number of nums)
         xor ^= number
      return xor
   };
}


const singleNonDuplicate = new Solution().singleNonDuplicate;
console.log(new Solution().singleNonDuplicate([1]) === 1)
console.log(new Solution().singleNonDuplicate([1, 2, 2]) === 1)
console.log(new Solution().singleNonDuplicate([1, 1, 2]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 3, 3]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) === 3)
console.log(new Solution().singleNonDuplicate([2, 2, 3, 3, 4]) === 4)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 3, 3, 4, 4, 5]) === 5)
console.log(new Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) === 10)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]) === 4)
