class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: greedy
    * @param {number[]} ratings
    * @return {number}
    */
   candy(ratings) {
      const candies = Array(ratings.length).fill(1);

      for (let index = 1; index < ratings.length; index++) {
         const prevRating = ratings[index - 1];
         const currentRating = ratings[index];
         if (prevRating < currentRating)
            candies[index] = candies[index - 1] + 1;
      }

      for (let index = ratings.length - 2; index > -1; index--) {
         const currentRating = ratings[index];
         const nextRating = ratings[index + 1];

         if (
            currentRating > nextRating &&
            candies[index] < candies[index + 1] + 1
         )
            candies[index] = candies[index + 1] + 1;
      }

      return candies.reduce((sum, num) => sum + num, 0)
   };
}


const candy = new Solution().candy;
console.log(new Solution().candy([1, 0, 2]) === 5)
console.log(new Solution().candy([1, 2, 2]) === 4)
console.log(new Solution().candy([1, 2, 3, 4]) === 10)
console.log(new Solution().candy([4, 3, 2, 1]) === 10)
