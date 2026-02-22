class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: two pointers
    * @param {string[]} chars
    * @return {number}
    */
   compress(chars) {
      let prevChar = null;
      chars.push(null);
      let counter = 0;
      let left = 0;

      for (const char of chars) {
         if (char === prevChar) {
            counter++;
            continue
         }

         if (counter > 1) {
            for (const digit of counter.toString()) {
               chars[left] = digit;
               left++;
            }
         }

         if (char) {
            chars[left] = char;
         }

         left++;
         prevChar = char;
         counter = 1;
      }

      chars.pop()
      return left - 1
      return chars
   };
}


const compress = new Solution().compress;
console.log(new Solution().compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']).toString() === ['a', '2', 'b', '2', 'c', '3', 'c'].toString())
console.log(new Solution().compress(['a']).toString() === ['a'].toString())
console.log(new Solution().compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']).toString() === ['a', 'b', '1', '2', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'].toString())
console.log(new Solution().compress(['a', 'a', 'a', 'b', 'b', 'a', 'a']).toString() === ['a', '3', 'b', '2', 'a', '2', 'a'].toString())
console.log(new Solution().compress(['v', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']).toString() === ['v', 'r', '9', 'r', 'r', 'r', 'r', 'r', 'r', 'r'].toString())
console.log(new Solution().compress(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']).toString() === ['a', '1', '0', '0', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'].toString())
