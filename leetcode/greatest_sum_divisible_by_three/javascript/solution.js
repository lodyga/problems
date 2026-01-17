class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      const dfs = (index, total) => {
         if (index === nums.length)
            return total % 3 === 0 ? total : 0

         const num = nums[index];
         const skip = dfs(index + 1, total);
         const take = dfs(index + 1, total + num);
         return Math.max(skip, take)
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      // Max subsequence sum divided by 3 with rest 0, 1, 2 respectively.
      const cache = [0, 0, 0];

      for (const num of nums) {
         for (const c of cache.slice()) {
            const mod = (c + num) % 3;
            cache[mod] = Math.max(cache[mod], c + num)
         }
      }
      return cache[0]
   }
}


const maxSumDivThree = new Solution().maxSumDivThree;
console.log(new Solution().maxSumDivThree([3]) === 3)
console.log(new Solution().maxSumDivThree([4]) === 0)
console.log(new Solution().maxSumDivThree([3, 6, 5, 1, 8]) === 18)
console.log(new Solution().maxSumDivThree([4]) === 0)
console.log(new Solution().maxSumDivThree([1, 2, 3, 4, 4]) === 12)
console.log(new Solution().maxSumDivThree([366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984, 787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]) === 50487)
