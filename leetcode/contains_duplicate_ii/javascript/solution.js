class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: sliding window 
    * @param {number[]} nums
    * @param {number} k
    * @return {boolean}
    */
   containsNearbyDuplicate(nums, k) {
      const window = new Set();

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];
         
         if (window.has(num))
            return true

         window.add(num);

         if (right >= k) {
            const leftNum = nums[right - k];
            window.delete(leftNum);
         }

      }
      return false
   }
}


const containsNearbyDuplicate = new Solution().containsNearbyDuplicate;
console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) === true)
console.log(new Solution().containsNearbyDuplicate([7, 8, 9, 9], 3) === true)
console.log(new Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) === true)
console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) === false)
console.log(new Solution().containsNearbyDuplicate([99, 99], 2) === true)
console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3) === true)
