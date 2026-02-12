class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   numOfSubarrays(nums) {
      const MOD = 10 ** 9 + 7;
      let prefix = 0;
      let res = 0;
      let oddCounter = 0;
      let evenCounter = 1;

      for (const num of nums) {
         prefix += num;

         if (prefix % 2) {
            res = (res + evenCounter) % MOD;
            oddCounter += 1;
         } else {
            res = (res + oddCounter) % MOD;
            evenCounter += 1;
         }
      }

      return res
   };
}


const numOfSubarrays = new Solution().numOfSubarrays;
console.log(new Solution().numOfSubarrays([3]) === 1)
console.log(new Solution().numOfSubarrays([1, 3, 5]) === 4)
console.log(new Solution().numOfSubarrays([2, 4, 6]) === 0)
console.log(new Solution().numOfSubarrays([1, 2, 3, 4]) === 6)
console.log(new Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) === 16)
