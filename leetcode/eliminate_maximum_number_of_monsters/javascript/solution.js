class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: sorting
    * @param {number[]} dist
    * @param {number[]} speed
    * @return {number}
    */
   eliminateMaximum(dist, speed) {
      const distance = dist.map((d, ind) => Math.ceil(d / speed[ind]));
      distance.sort((a, b) => a - b);

      for (let timeStamp = 0; timeStamp < distance.length; timeStamp++) {
         if (distance[timeStamp] <= timeStamp) {
            return timeStamp
         }
      }

      return distance.length
   };
}


const eliminateMaximum = new Solution().eliminateMaximum;
console.log(new Solution().eliminateMaximum([1, 3, 4], [1, 1, 1]) === 3)
console.log(new Solution().eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]) === 1)
console.log(new Solution().eliminateMaximum([3, 2, 4], [5, 3, 2]) === 1)
console.log(new Solution().eliminateMaximum([4, 3, 3, 3, 4], [1, 1, 1, 1, 4]) === 3)
console.log(new Solution().eliminateMaximum([46, 33, 44, 42, 46, 36, 7, 36, 31, 47, 38, 42, 43, 48, 48, 25, 28, 44, 49, 47, 29, 32, 30, 6, 42, 9, 39, 48, 22, 26, 50, 34, 40, 22, 10, 45, 7, 43, 24, 18, 40, 44, 17, 39, 36], [1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 3, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 8, 1, 1, 1, 3, 6, 1, 3, 1, 1]) === 7)
