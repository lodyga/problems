class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {boolean}
    */
   isBalanced(root) {
      let isTreeBalanced = true;

      function dfs(node) {
         if (!node || !isTreeBalanced) {
            return 0
         }
         const leftPath = dfs(node.left);
         const rightPath = dfs(node.right);
         if (Math.abs(leftPath - rightPath) > 1) {
            isTreeBalanced = false
            return 0
         }
         return 1 + Math.max(leftPath, rightPath)
      }
      dfs(root);
      return isTreeBalanced
   };
}


console.log(new Solution().isBalanced(buildTree([1, 2, 3])), true)
console.log(new Solution().isBalanced(buildTree([3, 9, 20, null, null, 15, 7])), true)
console.log(new Solution().isBalanced(buildTree([1, 2, 2, 3, 3, null, null, 4, 4])), false)
console.log(new Solution().isBalanced(buildTree([1, 2, 2, 3, null, null, 3, 4, null, null, 4])), false)