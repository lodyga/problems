class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: two pointers, sorting
    * @param {number[]} nums
    * @return {number[][]}
    */
   threeSum(nums) {
      nums.sort((a, b) => a - b);
      const res = [];

      for (let left = 0; left < nums.length - 2; left++) {
         const leftNum = nums[left];

         if (leftNum > 0) break

         // Skip repeating sequences with repeating left number.
         if (left && nums[left - 1] === leftNum) continue

         let mid = left + 1;
         let right = nums.length - 1;

         while (mid < right) {
            const triplet = leftNum + nums[mid] + nums[right];

            if (triplet === 0) {
               res.push([leftNum, nums[mid], nums[right]]);
               mid++;
               right--;

               // Skip repeating sequences with repeating middle number.
               while (mid < right && nums[mid - 1] === nums[mid]) {
                  mid++;
               }
            } else if (triplet > 0) {
               right--;
            } else {
               mid++;
            }
         }
      }

      return res
   };
}


const threeSum = new Solution().threeSum;
console.log(new Solution().threeSum([-1, 0, 1, 2, -1, -4]).toString() === [[-1, -1, 2], [-1, 0, 1]].toString())
console.log(new Solution().threeSum([3, 0, -2, -1, 1, 2]).toString() === [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]].toString())
console.log(new Solution().threeSum([1, 1, -2]).toString() === [[-2, 1, 1]].toString())
console.log(new Solution().threeSum([-1, 1, 1]).toString() === [].toString())
console.log(new Solution().threeSum([-2, 0, 0, 2, 2]).toString() === [[-2, 0, 2]].toString())
console.log(new Solution().threeSum([0, 0, 0]).toString() === [[0, 0, 0]].toString())
console.log(new Solution().threeSum([0, 0, 0, 0]).toString() === [[0, 0, 0]].toString())
