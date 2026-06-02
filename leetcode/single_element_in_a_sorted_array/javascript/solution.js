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
         const mid = Math.floor((left + right) / 2);
         const midNum = nums[mid];

         if (left === right) {
            return midNum;
         } else if (midNum == nums[mid + 1]) {
            if ((right - mid) % 2 === 0) {
               left = mid + 2;
            } else {
               right = mid - 1;
            }
         } else if (midNum === nums[mid - 1]) {
            if ((mid - left) % 2 === 0) {
               right = mid - 2;
            } else {
               left = mid + 1;
            }
         } else {
            return midNum;
         }
      }
   }
}


class Solution {
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
   
      for (const num of nums) {
         xor ^= num;
      }
   
      return xor;
   }
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
