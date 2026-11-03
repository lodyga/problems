class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: two pointers, iteration
    * @param {characters[]} letters
    * @return {void}
    */
   reverseString(letters) {
      let left = 0;
      let right = letters.length - 1;

      while (left < right) {
         [letters[left], letters[right]] = [letters[right], letters[left]];
         left++;
         right--;
      }
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: built-in function
    * @param {characters[]} letters
    * @return {void}
    */
   reverseString(letters) {
      return letters.reverse();
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *    A: two pointers, recursion
    * @param {characters[]} letters
    * @return {void}
    */
   reverseString(letters) {
      const dfs = (left, right) => {
         if (left >= right) {
            return;
         }

         [letters[left], letters[right]] = [letters[right], letters[left]];
         dfs(left + 1, right - 1);
      };

      dfs(0, letters.length - 1);
   }
}


const reverseString = new Solution().reverseString;
console.log(JSON.stringify(new Solution().reverseString(['h', 'e', 'l', 'l', 'o'])) === JSON.stringify(['o', 'l', 'l', 'e', 'h']))
console.log(JSON.stringify(new Solution().reverseString(['H', 'a', 'n', 'n', 'a', 'h'])) === JSON.stringify(['h', 'a', 'n', 'n', 'a', 'H']))
