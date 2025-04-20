class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number[]}
    */
   postorderTraversal(root) {
      const nodeList = [];

      function dfs(node) {
         if (!node) {
            return
         }
         dfs(node.left);
         dfs(node.right);
         nodeList.push(node.val);
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
   postorderTraversal(root) {
      const nodeList = [];
      const stack = [];
      let node = root;

      while (stack.length || node) {
         if (node) {
            nodeList.push(node.val);
            stack.push(node);
            node = node.right;
         }
         else {
            // Backtrack to the last right child
            node = stack.pop();
            node = node.left;
         }
      }
      nodeList.reverse();
      return nodeList
   };
}


console.log(new Solution().postorderTraversal(buildTree([])), [])
console.log(new Solution().postorderTraversal(buildTree([1])), [1])
console.log(new Solution().postorderTraversal(buildTree([1, null, 2, 3])), [3, 2, 1])
console.log(new Solution().postorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9])), [4, 6, 7, 5, 2, 9, 8, 3, 1])