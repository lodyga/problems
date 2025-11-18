class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   addToArrayForm(nums, k) {
      nums.reverse();
      let index = 0;
      while (k) {
         if (index == nums.length)
            nums.push(0);
         nums[index] += k % 10;
         k = parseInt(k / 10);
         if (nums[index] > 9) {
            k += 1;
            nums[index] -= 10;
         }
         index += 1;
      }
      nums.reverse();
      return nums
   };
}


const addToArrayForm = new Solution().addToArrayForm;
console.log(new Solution().addToArrayForm([1, 2, 0, 0], 34), [1, 2, 3, 4])
console.log(new Solution().addToArrayForm([2, 7, 4], 181), [4, 5, 5])
console.log(new Solution().addToArrayForm([2, 1, 5], 806), [1, 0, 2, 1])
console.log(new Solution().addToArrayForm([9, 9], 1), [1, 0, 0])
