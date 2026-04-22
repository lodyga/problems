class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} target
    * @param {number[]} arr
    * @return {boolean}
    */
   canBeEqual(target, arr) {
      const numFreq = Array(1000).fill(0);

      for (const num of target) {
         numFreq[num - 1]++;
      }

      for (const num of arr) {
         if (numFreq[num - 1] === 0) {
            return false
         }

         numFreq[num - 1]--;
      }

      return true
   };
}


const canBeEqual = new Solution().canBeEqual;
console.log(new Solution().canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]) === true)
console.log(new Solution().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]) === true)
console.log(new Solution().canBeEqual([7], [7]) === true)
console.log(new Solution().canBeEqual([3, 7, 9], [3, 7, 11]) === false)
