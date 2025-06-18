class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} plots
    * @param {number} flowersToPlant
    * @return {boolean}
    */
   canPlaceFlowers(plots, flowersToPlant) {
      if (flowersToPlant == 0) {
         return true
      }
      plots.push(0, 1);
      let contiguousEmptyPlots = 1;
      let flowerPlots = 0;

      for (let index = 0; index < plots.length; index++) {
         if (plots[index]) {
            if (contiguousEmptyPlots > 2) {
               // 1->0; 2->0; 3->1; 4->1; 5->2; 6->2; 7->3; 8->3; 9->4; 10->4
               flowerPlots += (contiguousEmptyPlots - 1) >> 1;
               if (flowerPlots >= flowersToPlant) {
                  return true
               }
            }
            contiguousEmptyPlots = 0;
         } else {
            contiguousEmptyPlots++;
         }
      }
      return false
   };
}
const canPlaceFlowers = new Solution().canPlaceFlowers;


console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1), true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2), false)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0], 1), true)
console.log(new Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0), true)
console.log(new Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1), true)
console.log(new Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2), true)
console.log(new Solution().canPlaceFlowers([0, 0, 0], 2), true)