class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: sorting, counting sort
    * @param {number[]} nums
    * @return {number}
    */
   minIncrementForUnique(nums) {
      let res = 0;
      let minNum = Math.min(...nums);
      const numFreq = new Map();
      let index = 0;

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      while (index < nums.length) {
         if (numFreq.has(minNum)) {
            const extras = numFreq.get(minNum) - 1;
            const nextNumFreq = (numFreq.get(minNum + 1) || 0) + extras;

            if (nextNumFreq) {
               numFreq.set(minNum + 1, nextNumFreq);
            }

            res += extras;
            index++;
         }

         minNum++;
      }

      return res
   };
}


const minIncrementForUnique = new Solution().minIncrementForUnique;
console.log(new Solution().minIncrementForUnique([1, 2, 2]) === 1)
console.log(new Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]) === 6)
console.log(new Solution().minIncrementForUnique([2, 2, 2, 1]) === 3)
console.log(new Solution().minIncrementForUnique([1, 3, 0, 3, 0]) === 3)
console.log(new Solution().minIncrementForUnique([13, 4, 12, 5, 3, 16, 11, 6, 11, 0, 2, 7, 19, 10, 1, 15, 15, 15, 11, 13]) === 25)
