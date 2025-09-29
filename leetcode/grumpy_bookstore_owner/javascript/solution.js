class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window
    * @param {number[]} customers
    * @param {number[]} grumpy
    * @param {number} minutes
    * @return {number}
    */
   maxSatisfied(customers, grumpy, minutes) {
      let satisfied = 0;
      let window = 0;
      let maxWindow = 0;
      let left = 0;

      for (let right = 0; right < customers.length; right++) {
         if (grumpy[right]) {
            window += customers[right];
         } else {
            satisfied += customers[right];
         }

         if (right - left + 1 < minutes) 
            continue

         maxWindow = Math.max(maxWindow, window);
         if (grumpy[left]) 
            window -= customers[left];
         left++;

      }
      return satisfied + maxWindow
   };
}


const maxSatisfied = new Solution().maxSatisfied;
console.log(new Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) === 16)
console.log(new Solution().maxSatisfied([1], [0], 1) === 1)
console.log(new Solution().maxSatisfied([4, 10, 10], [1, 1, 0], 2) == 24)