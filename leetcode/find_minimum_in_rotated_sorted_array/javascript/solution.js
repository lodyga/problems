class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} nums
    * @return {number}
    */
   findMin(nums) {
      let left = 0;
      let right = nums.length - 1;
      let res = nums[0];

      while (left < right) {
         // early exit
         if (nums[left] < nums[right]) {
            return Math.min(res, nums[left])
         }

         const mid = Math.floor((left + right)/2);
         const midNum = nums[mid];
         
         if (midNum < nums[right]) {
            res = Math.min(res, midNum);
            right = mid - 1;
         } else {
            res = Math.min(res, nums[right]);
            left = mid + 1;
         }
      }

      return res
   };
}


const findMin = new Solution().findMin;
console.log(new Solution().findMin([1, 2, 3, 4]) === 1)
console.log(new Solution().findMin([4, 1, 2, 3]) === 1)
console.log(new Solution().findMin([2, 3, 4, 1]) === 1)
console.log(new Solution().findMin([3, 4, 1, 2]) === 1)
console.log(new Solution().findMin([4, 5, 1, 2, 3]) === 1)
console.log(new Solution().findMin([5, 1, 2, 3, 4]) === 1)
console.log(new Solution().findMin([1, 2, 3, 4, 5]) === 1)
console.log(new Solution().findMin([2, 3, 4, 5, 1]) === 1)
console.log(new Solution().findMin([3, 4, 5, 1, 2]) === 1)
console.log(new Solution().findMin([4, 5, 6, 7, 0, 1, 2]) === 0)
console.log(new Solution().findMin([11, 13, 15, 17]) === 11)
console.log(new Solution().findMin([1]) === 1)
console.log(new Solution().findMin([3, 1, 2]) === 1)
