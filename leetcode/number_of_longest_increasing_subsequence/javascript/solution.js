class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   findNumberOfLIS(numbers) {
      const cache = Array.from({length: numbers.length}, () => [1, 1]);
      let lisLength = 1;

      for (let right = 1; right < numbers.length; right++) {
         for (let left = 0; left < right; left++) {
            const [prevLength, prevFrequency] = cache[left];
            
            if (numbers[left] < numbers[right]) {
               if (prevLength + 1 > cache[right][0]) {
                  cache[right] = [prevLength + 1, prevFrequency];
                  lisLength = Math.max(lisLength, prevLength + 1);
               } else if (prevLength + 1 === cache[right][0]) {
                  cache[right] = [cache[right][0], cache[right][1] + prevFrequency];
               }
            }
         }
      }
      let lisCounter = 0
      for (const [sequenceLength, frequency] of cache) {
         if (sequenceLength === lisLength) {
            lisCounter += frequency
         }
      }
      return lisCounter
   };
}


console.log(new Solution().findNumberOfLIS([1, 3, 5, 4]) === 2)  // [1, 3, 4] and [1, 3, 5]
console.log(new Solution().findNumberOfLIS([1, 3, 5, 4, 7]) === 2)  // [1, 3, 4, 7] and [1, 3, 5, 7]
console.log(new Solution().findNumberOfLIS([2, 2, 2, 2, 2]) === 5)  // [2] * 5
console.log(new Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) === 3)  // [1, 2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 4, 5, 7]
console.log(new Solution().findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]) === 27)