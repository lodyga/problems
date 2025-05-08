class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} numbers
    * @return {number}
    */
   maxProductDifference(numbers) {
      let minNumber = numbers[0];
      let almostMinNumber = numbers[0];
      let maxNumber = numbers[0];
      let almostMaxNumber = numbers[0];

      for (const number of numbers) {
         if (number > maxNumber)
            [maxNumber, almostMaxNumber] = [number, maxNumber];
         else if (number > almostMaxNumber)
            almostMaxNumber = number;
         else if (number < minNumber)
            [minNumber, almostMinNumber] = [number, minNumber];
         else if (number < almostMinNumber)
            almostMinNumber = number;
      }
      return maxNumber * almostMaxNumber - minNumber * almostMinNumber
   };
}


console.log(new Solution().maxProductDifference([5, 6, 2, 7, 4]), 34)
console.log(new Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]), 64)