class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search, greedy
    * @param {number[]} houses
    * @param {number} k
    * @return {number}
    */
   minCapability(houses, k) {
      const validateCapability = (capability) => {
         let index = 0;
         let robbedHouses = 0;
         while (index < houses.length) {
            if (houses[index] <= capability) {
               robbedHouses++;
               index += 2;
               if (robbedHouses >= k) {
                  return true
               }
            } else {
               index++;
            }
         }
         return false
      };

      const sortedCapabilities = [...houses].sort((a, b) => a - b);
      let left = 0;
      let right = houses.length - 1;
      let minCap = sortedCapabilities[right];

      while (left <= right) {
         const middle = (left + right) >> 1;
         const capability = sortedCapabilities[middle]

         if (validateCapability(capability)) {
            minCap = sortedCapabilities[middle];
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return minCap
   };
}


const minCapability = new Solution().minCapability;
console.log(new Solution().minCapability([2, 2], 1) === 2)
console.log(new Solution().minCapability([1, 4, 5], 1) === 1)
console.log(new Solution().minCapability([2, 3, 5, 9], 2) === 5)
console.log(new Solution().minCapability([2, 7, 9, 3, 1], 2) === 2)
console.log(new Solution().minCapability([5038, 3053, 2825, 3638, 4648, 3259, 4948, 4248, 4940, 2834, 109, 5224, 5097, 4708, 2162, 3438, 4152, 4134, 551, 3961, 2294, 3961, 1327, 2395, 1002, 763, 4296, 3147, 5069, 2156, 572, 1261, 4272, 4158, 5186, 2543, 5055, 4735, 2325, 1206, 1019, 1257, 5048, 1563, 3507, 4269, 5328, 173, 5007, 2392, 967, 2768, 86, 3401, 3667, 4406, 4487, 876, 1530, 819, 1320, 883, 1101, 5317, 2305, 89, 788, 1603, 3456, 5221, 1910, 3343, 4597], 28) === 4134)