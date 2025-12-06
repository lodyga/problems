class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @return {boolean}
    */
   containsDuplicate(nums) {
      const numSet = new Set();
      for (const num of nums) {
         if (numSet.has(num)) {
            return true
         } else {
            numSet.add(num);
         }
      }
      return false
   };
}


class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: One-liner
    * @param {number[]} nums
    * @return {boolean}
   */
   containsDuplicate(nums) {
      return nums.length !== (new Set(nums)).size
   };
}


const containsDuplicate = new Solution().containsDuplicate;
console.log(new Solution().containsDuplicate([1, 2, 3]) === false)
console.log(new Solution().containsDuplicate([1, 2, 3, 4]) === false)
console.log(new Solution().containsDuplicate([1, 2, 3, 1]) === true)
console.log(new Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) === true)
