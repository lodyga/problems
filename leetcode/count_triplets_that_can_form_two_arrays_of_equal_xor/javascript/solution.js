class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: bit manipulation, prefix sum
    * @param {number[]} nums
    * @return {}
    */
   countTriplets(nums) {
      const prefix = [0];
      let res = 0;

      for (const num of nums) {
         prefix.push(prefix[prefix.length - 1] ^ num);
      }

      for (let k = 0; k < nums.length; k++) {
         for (let j = 0; j < k + 1; j++) {
            for (let i = 0; i < j; i++) {
               // if ((prefix[i] ^ prefix[j - 1]) === (prefix[k + 1] ^ prefix[j - 1])) {
               if (prefix[i] === prefix[k + 1]) {
                  res++;
               }
            }
         }
      }

      return res
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: bit manipulation, prefix sum
    * @param {number[]} nums
    * @return {}
    */
   countTriplets(nums) {
      const prefix = [0];
      let res = 0;

      for (const num of nums) {
         prefix.push(prefix[prefix.length - 1] ^ num);
      }

      for (let right = 0; right < nums.length + 1; right++) {
         for (let left = 0; left < right; left++) {
            if (prefix[left] === prefix[right]) {
               res += right - left - 1;
            }
         }
      }

      return res
   };
}


const countTriplets = new Solution().countTriplets;
console.log(new Solution().countTriplets([2, 3, 1, 6, 7]) === 4)
console.log(new Solution().countTriplets([1, 1, 1, 1, 1]) === 10)
console.log(new Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]) === 8)
