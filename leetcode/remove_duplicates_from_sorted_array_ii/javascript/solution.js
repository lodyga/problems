class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: two pointers
    * @param {number[]} nums
    * @return {number}
    */
   removeDuplicates(nums) {
      let left = 1;

      for (let right = 2; right < nums.length; right++) {
         if (nums[left - 1] === nums[right]) {
            continue
         } else {
            left++;
            [nums[left],  nums[right]] = [nums[right],  nums[left]];
         }
      }
      return left + 1
   };
}


const removeDuplicates = new Solution().removeDuplicates;
console.log(new Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5)
console.log(new Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) === 7)
