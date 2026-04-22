class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   countBadPairs(nums) {
      const N = nums.length;
      const diffMap = new Map();

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         const diff = num - index;

         if (!diffMap.has(diff)) {
            diffMap.set(diff, []);
         }

         diffMap.get(diff).push(index);
      }

      const totalPairs = (N - 1) * N / 2;
      const arr = [];

      for (const vals of diffMap.values()) {
         if (vals.length > 1) {
            arr.push(vals.length)
         }
      }

      const good_pairs = arr.map((val) => (val - 1) * val / 2).reduce((sum, val) => sum + val, 0)
      return totalPairs - good_pairs
   };
}


const countBadPairs = new Solution().countBadPairs;
console.log(new Solution().countBadPairs([4, 1, 3, 3]) === 5)
console.log(new Solution().countBadPairs([1, 2, 3, 4, 5]) === 0)
