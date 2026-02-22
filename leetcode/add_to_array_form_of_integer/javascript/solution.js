class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   addToArrayForm(nums, k) {
      nums.reverse();
      let index = 0;

      while (k) {
         if (index == nums.length) {
            nums.push(0);
         }

         nums[index] += k % 10;
         k = Math.floor(k / 10);
         
         if (nums[index] > 9) {
            nums[index] -= 10;
            k += 1;
         }

         index += 1;
      }
      
      nums.reverse();
      return nums
   };
}


const addToArrayForm = new Solution().addToArrayForm;
console.log(new Solution().addToArrayForm([1, 2, 0, 0], 34).toString() === [1, 2, 3, 4].toString())
console.log(new Solution().addToArrayForm([2, 7, 4], 181).toString() === [4, 5, 5].toString())
console.log(new Solution().addToArrayForm([2, 1, 5], 806).toString() === [1, 0, 2, 1].toString())
console.log(new Solution().addToArrayForm([9, 9], 1).toString() === [1, 0, 0].toString())
