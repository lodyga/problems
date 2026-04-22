class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: hash map
    *     A: prefix sum
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   subarraysDivByK(nums, k) {
      // prefix sum mod
      let mod = 0;
      const seen = new Map([[0, 1]]);
      let res = 0;

      for (let num of nums) {
         if (num < 0) {
            num = (num % k) + k;
         }

         mod = (mod + num) % k;

         if (seen.has(mod)) {
            res += seen.get(mod);
            seen.set(mod, seen.get(mod) + 1);
         } else {
            seen.set(mod, 1);
         }
      }

      return res
   };
}


const subarraysDivByK = new Solution().subarraysDivByK;
console.log(new Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) === 7)
console.log(new Solution().subarraysDivByK([5], 9) === 0)
console.log(new Solution().subarraysDivByK([-1, 2, 9], 2) === 2)
console.log(new Solution().subarraysDivByK([7, 4, -10], 5) === 1)
