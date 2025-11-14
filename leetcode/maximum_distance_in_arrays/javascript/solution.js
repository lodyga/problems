class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number[][]} arrays
    * @return {number}
    */
   maxDistance(arrays) {
      let minNumber = arrays[0][0];
      let maxNumber = arrays[0][arrays[0].length - 1];
      let maxDistance = 0;

      for (let index = 1; index < arrays.length; index++) {
         let currentMin = arrays[index][0];
         let currentMax = arrays[index][arrays[index].length - 1];
         maxDistance = Math.max(
            maxDistance,
            currentMax - minNumber,
            maxNumber - currentMin
         )
         minNumber = Math.min(minNumber, currentMin)
         maxNumber = Math.max(maxNumber, currentMax)
      }

      return maxDistance
   };
}


const maxDistance = new Solution().maxDistance;
console.log(new Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) === 4)
console.log(new Solution().maxDistance([[1], [1]]) === 0)
