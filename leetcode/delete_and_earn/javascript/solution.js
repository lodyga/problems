class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   deleteAndEarn(numbers) {
      const numberFrequency = new Map();
      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
      }

      const uniqueSortedNumbers = [...new Set(numbers)].sort((a, b) => a - b);
      const cache = Array(uniqueSortedNumbers.length).fill(0);

      for (let index = 0; index < uniqueSortedNumbers.length; index++) {
         const number = uniqueSortedNumbers[index];
         cache[index] = number * numberFrequency.get(number);

         if (index === 0) {
            continue
         } else if (uniqueSortedNumbers[index - 1] + 1 === number) {
            cache[index] = Math.max(
               cache[index] + (index !== 1 ? cache[index - 2] : 0),
               cache[index - 1]
            )
         } else {
            cache[index] += cache[index - 1];
         }
      }
      return cache[cache.length - 1]
   };
}


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * cache optimized
    * @param {number[]} numbers
    * @return {number}
    */
   deleteAndEarn(numbers) {
      const numberFrequency = new Map();
      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
      }

      const uniqueSortedNumbers = [...new Set(numbers)].sort((a, b) => a - b);
      const cache = [0, 0];

      for (let index = 0; index < uniqueSortedNumbers.length; index++) {
         const number = uniqueSortedNumbers[index];
         let currentCache = number * numberFrequency.get(number);

         if (index === 0) {
            [cache[0], cache[1]] = [0, currentCache];
            continue
         } else if (uniqueSortedNumbers[index - 1] + 1 === number) {
            currentCache = Math.max(
               currentCache + (index !== 1 ? cache[0] : 0),
               cache[1]
            )
         } else {
            currentCache += cache[1];
         }
         [cache[0], cache[1]] = [cache[1], currentCache];
      }
      return cache[cache.length - 1]
   };
}


console.log(new Solution().deleteAndEarn([1]) === 1)
console.log(new Solution().deleteAndEarn([2, 3]) === 3)
console.log(new Solution().deleteAndEarn([2, 4]) === 6)
console.log(new Solution().deleteAndEarn([3, 4, 2]) === 6)
console.log(new Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) === 9)
console.log(new Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) === 37)
console.log(new Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]) === 18)
console.log(new Solution().deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]) === 43)
console.log(new Solution().deleteAndEarn([1, 1, 1]) === 3)
console.log(new Solution().deleteAndEarn([12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) === 3451)