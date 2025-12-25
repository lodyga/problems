class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack, string
    *     A: iteration
    * @param {string} path
    * @return {string}
    */
   simplifyPath(path) {
      const stack = [];
      let name = '';

      for (const char of path + '/') {
         if (char === '/') {
            if (name === '..') {
               if (stack.length) {
                  stack.pop();
               }
            } else if (name && name !== '.') {
               stack.push(name);
            }
            name = '';
         } else {
            name += char;
         }
      }
      return '/' + stack.join('/')
   };
}


const simplifyPath = new Solution().simplifyPath;
console.log(new Solution().simplifyPath('/home/') === '/home')
console.log(new Solution().simplifyPath('/home//foo/') === '/home/foo')
console.log(new Solution().simplifyPath('/home/user/Documents/../Pictures') === '/home/user/Pictures')
console.log(new Solution().simplifyPath('/../') === '/')
console.log(new Solution().simplifyPath('/.../a/../b/c/../d/./') === '/.../b/d')
console.log(new Solution().simplifyPath('/a/../../b/../c//.//') === '/c')
console.log(new Solution().simplifyPath('/.') === '/')
console.log(new Solution().simplifyPath('/..hidden') === '/..hidden')
