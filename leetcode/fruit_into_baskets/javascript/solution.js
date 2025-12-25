class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: hash map
    *     A: sliding window
    * @param {number[]} fruits
    * @return {number}
    */
   totalFruit(fruits) {
      let left = 0;
      const window = new Map();
      let total = 0;

      for (let right = 0; right < fruits.length; right++) {
         const fruit = fruits[right];
         window.set(fruit, (window.get(fruit) || 0) + 1);

         while (window.size > 2) {
            const leftFruit = fruits[left];
            window.set(leftFruit, window.get(leftFruit) - 1);
            if (window.get(leftFruit) === 0) {
               window.delete(leftFruit);
            }
            left++;
         }
         total = Math.max(total, right - left + 1);
      }
      return total
   };
}


const totalFruit = new Solution().totalFruit;
console.log(new Solution().totalFruit([1, 2, 1]) === 3)
console.log(new Solution().totalFruit([0, 1, 2, 2]) === 3)
console.log(new Solution().totalFruit([1, 2, 3, 2, 2]) === 4)
console.log(new Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) === 5)
console.log(new Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]) === 5)
