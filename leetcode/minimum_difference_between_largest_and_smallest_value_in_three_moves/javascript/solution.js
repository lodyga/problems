class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {number[]} numbers
    * @return {number}
    */
   minDifference(numbers) {
      if (numbers.length <= 4)
            return 0

        numbers.sort((a, b) => a - b);
        const len = numbers.length;
        
        return Math.min(
            numbers[len - 4] - numbers[0],
            numbers[len - 3] - numbers[1],
            numbers[len - 2] - numbers[2],
            numbers[len - 1] - numbers[3]
        )
   };
}


const minDifference = new Solution().minDifference;
console.log(new Solution().minDifference([5, 3, 2, 4]) === 0);
console.log(new Solution().minDifference([1, 5, 0, 10, 14]) === 1);
console.log(new Solution().minDifference([3, 100, 20]) === 0);
console.log(new Solution().minDifference([90, 35, 67, 53, 61]) === 6);