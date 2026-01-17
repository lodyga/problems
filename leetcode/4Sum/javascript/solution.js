class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n)
    * Tags:
    *    A: two pointers
    * @param {number[]} nums
    * @param {number} target
    * @return {}
    */
   fourSum(nums, target) {
      nums.sort((a, b) => a - b);
      const quadruplets = [];

      for (let i = 0; i < nums.length - 3; i++) {
         if (nums[i - 1] === nums[i])
            continue

         for (let j = i + 1; j < nums.length - 2; j++) {
            if (j > i + 1 && nums[j - 1] === nums[j])
               continue

            let left = j + 1;
            let right = nums.length - 1;

            while (left < right) {
               const quadruplet = nums[i] + nums[j] + nums[left] + nums[right]
               
               if (quadruplet === target) {
                  quadruplets.push([nums[i], nums[j], nums[left], nums[right]])
                  left++;
                  right--;
                  while (left < right && nums[left - 1] === nums[left])
                     left++;
               } else if (quadruplet < target)
                  left++;
               else
                  right--;
            }
         }
      }
      return quadruplets
   };
}


const fourSum = new Solution().fourSum;
console.log(JSON.stringify(new Solution().fourSum([1, 0, -1, 0, -2, 2], 0)) === JSON.stringify([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
console.log(JSON.stringify(new Solution().fourSum([2, 2, 2, 2, 2], 8)) === JSON.stringify([[2, 2, 2, 2]]))
console.log(JSON.stringify(new Solution().fourSum([0, 0, 0, 0], 0)) === JSON.stringify([[0, 0, 0, 0]]))
console.log(JSON.stringify(new Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)) === JSON.stringify([[-5, -4, -3, 1]]))
