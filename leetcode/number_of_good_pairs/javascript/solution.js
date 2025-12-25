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
   numIdenticalPairs(nums) {
      const numFreq = new Map();
      let counter = 0;

      for (const number of nums) {
         numFreq.set(number, (numFreq.get(number) || 0) + 1);
      }

      for (const freq of numFreq.values()) {
         counter += parseInt(freq * (freq - 1) / 2);
      }
      return counter
   };
}


const numIdenticalPairs = new Solution().numIdenticalPairs;
console.log(new Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) === 4)
console.log(new Solution().numIdenticalPairs([1, 1, 1, 1]) === 6)
console.log(new Solution().numIdenticalPairs([1, 2, 3]) === 0)
