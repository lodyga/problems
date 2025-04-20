class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number[]}
    */
   inorderTraversal(root) {
      const nodeList = [];

      function dfs(node) {
         if (!node) {
            return
         }
         dfs(node.left);
         nodeList.push(node.val);
         dfs(node.right);
      }
      dfs(root);
      return nodeList
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iterative, stack
    * @param {TreeNode} root
    * @return {number[]}
    */
   inorderTraversal(root) {
      const nodeList = [];
      const stack = [];
      let node = root;

      while (node || stack.length) {
         while (node) {
            stack.push(node);
            node = node.left;
         }
         node = stack.pop();
         nodeList.push(node.val);
         node = node.right;
      }
      return nodeList
   };
}

   
console.log(new Solution().inorderTraversal(buildTree([])), [])
console.log(new Solution().inorderTraversal(buildTree([1])), [1])
console.log(new Solution().inorderTraversal(buildTree([1, null, 2, 3])), [1, 3, 2])
console.log(new Solution().inorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9])), [4, 2, 6, 5, 7, 1, 3, 9, 8])