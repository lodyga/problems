class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers
    * @return {number}
    */
   longestConsecutive(numbers) {
      const numberSet = new Set(numbers);
      let longestConsec = 1;

      for (const number of numberSet) {
         if (!numberSet.has(number - 1)) {
            let index = 1;
            while (numberSet.has(number + index))
               index++;
            longestConsec = Math.max(longestConsec, index);
         }
      }
      return longestConsec
   };
}
const longestConsecutive = new Solution().longestConsecutive;


console.log(new Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
console.log(new Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
console.log(new Solution().longestConsecutive([1, 0, 1, 2]), 3)