class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
   searchRange(nums, target) {
      const bisect = (nums, target, direction) => {
         let left = 0;
         let right = nums.length - 1;
         let res = -1;

         while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const midNum = nums[mid];

            if (target === midNum) {
               res = mid;

               if (direction === 'left') {
                  right = mid - 1;
               }
               else {  // else if (direction === 'right'):
                  left = mid + 1;
               }
            }
            else if (target < midNum) {
               right = mid - 1;
            }
            else {
               left = mid + 1;
            }
         }

         return res;
      }

      const bisectLeft = (nums, target) => {
         return bisect(nums, target, 'left')
      };

      const bisectRight = (nums, target) => {
         return bisect(nums, target, 'right')
      };

      const leftBisect = bisectLeft(nums, target);
      const rightBisect = bisectRight(nums, target);

      return [leftBisect, rightBisect];
   }
}


const searchRange = new Solution().searchRange;
console.log(new Solution().searchRange([5, 5, 7], 5).toString() === [0, 1].toString())
console.log(new Solution().searchRange([5, 7, 7], 7).toString() === [1, 2].toString())
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 8).toString() === [3, 4].toString())
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 6).toString() === [-1, -1].toString())
console.log(new Solution().searchRange([], 0).toString() === [-1, -1].toString())
console.log(new Solution().searchRange([1], 1).toString() === [0, 0].toString())
