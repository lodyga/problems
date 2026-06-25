class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} nums
    * @param {number} k
    * @param {number} target
    * @return {number[]}
    */
   findClosestElements(nums, k, target) {
      let left = 0;
      let right = nums.length - k;

      while (left < right) {
         const mid = Math.floor((left + right) / 2);

         if (target - nums[mid] <= nums[mid + k] - target) {
            right = mid - 1;
         }
         else {
            left = mid + 1;
         }
      }

      return nums.slice(left, left + k);
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {number[]} nums
    * @param {number} k
    * @param {number} target
    * @return {number[]}
    */
   findClosestElements(nums, k, target) {
      let left = 0;
      let right = nums.length - 1;

      while (right - left + 1 > k) {
         if (target - nums[left] <= nums[right] - target) {
            right--;
         } else {
            left++;
         }
      }

      return nums.slice(left, right + 1);
   }
}


const findClosestElements = new Solution().findClosestElements;
console.log(new Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3).toString() === [1, 2, 3, 4].toString())
console.log(new Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1).toString() === [1, 1, 2, 3].toString())
console.log(new Solution().findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9).toString() === [3, 6, 8, 8, 9].toString())
