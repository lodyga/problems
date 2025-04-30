class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, iteration
    * @param {characters[]} letters
    * @return {characters[]}
    */
   reverseString(letters) {
      let left = 0;
      let right = letters.length - 1;

      while (left < right) {
         [letters[left], letters[right]] = [letters[right], letters[left]];
         left++;
         right--;
      }
      return letters
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers, recursion
    * @param {characters[]} letters
    * @return {characters[]}
    */
   reverseString(letters) {
      function dfs(left, right) {
         if (left < right) {
            [letters[left], letters[right]] = [letters[right], letters[left]];
            dfs(left + 1, right - 1)
         }
      }
      dfs(0, letters.length - 1)
      return letters
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: build-in function
    * @param {characters[]} letters
    * @return {characters[]}
    */
   reverseString(letters) {
      return letters.reverse()
   };
}


console.log(new Solution().reverseString(["h", "e", "l", "l", "o"]), ["o", "l", "l", "e", "h"])
console.log(new Solution().reverseString(["H", "a", "n", "n", "a", "h"]), ["h", "a", "n", "n", "a", "H"])