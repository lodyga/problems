class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string} path
    * @return {string}
    */
   simplifyPath(path) {
      const stack = [];
      let word = '';

      for (const char of path + '/') {
         if (char === '/') {
            if (word === '..') {
               if (stack.length) {
                  stack.pop();
               }
            } else if (word && word !== '.') {
               stack.push(word);
            }
            word = '';
         } else {
            word += char;
         }
      }
      return '/' + stack.join('/')
   };
}



console.log(new Solution().simplifyPath('/home/') === '/home')
console.log(new Solution().simplifyPath('/home//foo/') === '/home/foo')
console.log(new Solution().simplifyPath('/home/user/Documents/../Pictures') === '/home/user/Pictures')
console.log(new Solution().simplifyPath('/../') === '/')
console.log(new Solution().simplifyPath('/.../a/../b/c/../d/./') === '/.../b/d')
console.log(new Solution().simplifyPath('/a/../../b/../c//.//') === '/c')
console.log(new Solution().simplifyPath('/.') === '/')
console.log(new Solution().simplifyPath('/..hidden') === '/..hidden')