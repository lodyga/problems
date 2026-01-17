class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: brute-force, prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   maxSumMinProduct(nums) {
      const MOD = BigInt(10 ** 9 + 7);
      let res = 0n;

      const prefix = [0n];
      for (const num of nums)
         prefix.push(prefix[prefix.length - 1] + BigInt(num));

      for (let left = 0; left < nums.length; left++) {
         let minNum = nums[left];
         let subarraySum = 0;

         for (let right = left; right < nums.length; right++) {
            minNum = Math.min(minNum, nums[right]);
            subarraySum = prefix[right + 1] - prefix[left];
            //res = Math.max(res, minNum * subarraySum);
            const candidate = BigInt(minNum) * subarraySum;
            if (candidate > res) res = candidate;
         }
      }
      return Number(res % MOD)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   maxSumMinProduct2(nums) {
      const MOD = BigInt(10 ** 9 + 7);
      let res = 0n;
      const stack = [];

      const prefix = [0n];
      for (const num of nums) {
         prefix.push(prefix[prefix.length - 1] + BigInt(num));
      }

      for (let index = 0; index < nums.length; index++) {
         let start = index;
         const num = nums[index];

         while (stack.length && stack[stack.length - 1][1] > num) {
            const [prevStart, val] = stack.pop();
            const subarraySum = prefix[index] - prefix[prevStart];
            const candidate = BigInt(val) * subarraySum;
            if (candidate > res) res = candidate;
            start = prevStart;
         }
         stack.push([start, num]);
      }

      while (stack.length) {
         const [start, val] = stack.pop();
         const subarraySum = prefix[nums.length] - prefix[start];
         const candidate = BigInt(val) * subarraySum;
         if (candidate > res) res = candidate;
      }

      return Number(res % MOD);
   };
}


const maxSumMinProduct = new Solution().maxSumMinProduct;
console.log(new Solution().maxSumMinProduct([1]) === 1)
console.log(new Solution().maxSumMinProduct([1, 2]) === 4)
console.log(new Solution().maxSumMinProduct([1, 2, 3]) === 10)
console.log(new Solution().maxSumMinProduct([1, 2, 3, 2]) === 14)
console.log(new Solution().maxSumMinProduct([2, 3, 3, 1, 2]) === 18)
console.log(new Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]) === 60)
