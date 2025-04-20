class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number[]}
    */
   preorderTraversal(root) {
      const nodeList = [];

      function dfs(node) {
         if (!node) {
            return
         }
         nodeList.push(node.val);
         dfs(node.left);
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
   preorderTraversal(root) {
      const nodeList = [];
      const stack = [];
      let node = root;

      while (stack.length || node) {
         if (node) {
            nodeList.push(node.val);
            stack.push(node.right);
            node = node.left;
         }
         else {
            // Backtrack to the last right child
            node = stack.pop();
         }
      }
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
   preorderTraversal(root) {
      if (!root) return [];
      const nodeList = [];
      const stack = [root];

      while (stack.length) {
         const stackLength = stack.length;

         for (let index = 0; index < stackLength; index++) {
            const node = stack.pop();
            nodeList.push(node.val);
            if (node.right) stack.push(node.right);
            if (node.left) stack.push(node.left);
         }
      }
      return nodeList
   };
}


console.log(new Solution().preorderTraversal(buildTree([])), [])
console.log(new Solution().preorderTraversal(buildTree([1])), [1])
console.log(new Solution().preorderTraversal(buildTree([1, null, 2, 3])), [1, 2, 3])
console.log(new Solution().preorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9])), [1, 2, 4, 5, 6, 7, 3, 8, 9])