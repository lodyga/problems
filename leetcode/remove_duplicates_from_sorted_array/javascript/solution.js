class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {number[]} nums
    * @return {number}
    */
   removeDuplicates(nums) {
      let left = 0;

      for (let right = 0; right < nums.length; right++) {
         if (nums[left] === nums[right]) {
            continue
         } else {
            left++;
            nums[left] = nums[right];
         }
      }
      return left + 1;
   };
}


const removeDuplicates = new Solution().removeDuplicates;
console.log(new Solution().removeDuplicates([1, 1, 2]) === 2)
console.log(new Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) === 5)
