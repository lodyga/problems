class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers, in-place method
    * @param {number[]} nums
    * @return {number[]}
    */
   sortArrayByParity(nums) {
      let left = 0;
      
      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];

         if (num % 2 === 0) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
         }
      }
      return nums
   };
}


const sortArrayByParity = new Solution().sortArrayByParity;
console.log(JSON.stringify(new Solution().sortArrayByParity([3, 1, 2, 4])) === JSON.stringify([2, 4, 3, 1]))
console.log(JSON.stringify(new Solution().sortArrayByParity([1, 2, 3, 4])) === JSON.stringify([2, 4, 3, 1]))
console.log(JSON.stringify(new Solution().sortArrayByParity([0])) === JSON.stringify([0]))
