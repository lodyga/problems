class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {number[]} numbers
    * @return {number[]}
    */
   replaceElements(numbers) {
      const numberList = [-1];
      let maxNumber = -1;

      for (const number of numbers.slice(1,).reverse()) {
         maxNumber = maxNumber > number ? maxNumber : number;
         numberList.push(maxNumber);
      }
      return numberList.reverse()
   };
}


const replaceElements = function (numbers) {
   const greatestRight = Array(numbers.length).fill(-1);
   const numbersReversed = numbers.reverse()

   for (let index = 0; index < numbers.length - 1; index++) {
      greatestRight[index + 1] = Math.max(greatestRight[index], numbersReversed[index]);
   }

   return greatestRight.reverse()
}


const replaceElements = function (numbers) {
   const greatestRight = Array(numbers.length).fill(-1);

   for (let index = numbers.length - 2; index >= 0; index--) {
      greatestRight[index] = Math.max(greatestRight[index + 1], numbers[index + 1]);
   }

   return greatestRight
}


const replaceElements = function (numbers) {
   numbers.shift();
   numbers.push(-1)

   for (let index = numbers.length - 2; index >= 0; index--) {
      numbers[index] = Math.max(numbers[index], numbers[index + 1]);
   }

   return numbers
}


console.log(new Solution().replaceElements([17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])
console.log(new Solution().replaceElements([400]), [-1])