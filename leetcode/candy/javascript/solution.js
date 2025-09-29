class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: greedy
    * @param {number[]} ratings
    * @return {number}
    */
   candy(ratings) {
      const candies = Array(ratings.length).fill(1);

      for (let index = 1; index < ratings.length; index++) {
         const currentRating = ratings[index];
         const prevRating = ratings[index - 1];
         if (currentRating > prevRating)
            candies[index] = candies[index - 1] + 1
      }
      
      let totalCandies = candies[candies.length - 1];
      for (let index = ratings.length - 2; index > -1; index--) {
         const currentRating = ratings[index];
         const nextRating = ratings[index + 1];
         if (currentRating > nextRating)
            candies[index] = Math.max(candies[index], candies[index + 1] + 1)
         totalCandies += candies[index]
      }

      return totalCandies
   };
}


const candy = new Solution().candy;
console.log(new Solution().candy([1, 0, 2]) === 5)
console.log(new Solution().candy([1, 2, 2]) === 4)
console.log(new Solution().candy([1, 2, 3, 4]) === 10)
console.log(new Solution().candy([4, 3, 2, 1]) === 10)