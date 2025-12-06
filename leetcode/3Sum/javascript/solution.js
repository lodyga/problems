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
      const triplets = [];

      let left = 0;
      while (left < nums.length - 2) {
         const leftNum = nums[left];

         // If left number is > 0 then triplet sum is > 0
         if (leftNum > 0) {
            break
         }
         // Skip duplicate left values.
         if (left && nums[left - 1] === leftNum) {
            left++;
            continue
         }

         let middle = left + 1;
         let right = nums.length - 1;

         while (middle < right) {
            const triplet = leftNum + nums[middle] + nums[right];

            if (triplet === 0) {
               triplets.push([leftNum, nums[middle], nums[right]]);
               middle++;
               right--;
               // Skip duplicate middle values.
               while (
                  middle < right &&
                  nums[middle - 1] === nums[middle]
               ) {
                  middle++;
               }
            } else if (triplet > 0) {
               right--;
            } else {
               middle++;
            }
         }
         left++;
      }
      return triplets
   };
}


const threeSum = new Solution().threeSum;
console.log(new Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
console.log(new Solution().threeSum([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
console.log(new Solution().threeSum([1, 1, -2]), [[-2, 1, 1]])
console.log(new Solution().threeSum([-1, 1, 1]), [])
console.log(new Solution().threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
console.log(new Solution().threeSum([0, 0, 0]), [[0, 0, 0]])
console.log(new Solution().threeSum([0, 0, 0, 0]), [[0, 0, 0]])
