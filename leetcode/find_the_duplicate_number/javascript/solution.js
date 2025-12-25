class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: two pointers, Floyd's cycle finding algorithm or Hare-Tortoise algorithm        
    * @param {number[]} numbers
    * @return {number}
    */
   findDuplicate(numbers) {
      let slow = 0;
      let fast = 0;

      while (true) {
         slow = numbers[slow];
         fast = numbers[numbers[fast]];
         if (slow === fast)
            break
      }

      let slow2 = 0;
      while (true) {
         slow = numbers[slow];
         slow2 = numbers[slow2];
         if (slow === slow2)
            return slow
      }
   };
}


const findDuplicate = new Solution().findDuplicate;
console.log(new Solution().findDuplicate([1, 3, 4, 2, 2]) === 2)
console.log(new Solution().findDuplicate([3, 1, 3, 4, 2]) === 3)
console.log(new Solution().findDuplicate([3, 3, 3, 3, 3]) === 3)
console.log(new Solution().findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) === 9)
console.log(new Solution().findDuplicate([2, 1, 2]) === 2)
