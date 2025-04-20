import { Queue } from '@datastructures-js/queue';

class TreeNode {
   constructor(val = null, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
   }
}

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      if (!root) {
         return null  // return, returns undefined
      }
      [root.left, root.right] = [root.right, root.left];
      this.invertTree(root.left);
      this.invertTree(root.right);

      return root
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, stack, iteration
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      if (!root) {
         return null
      }

      const stack = [root];
      while (stack.length) {
         const node = stack.pop();
         [node.left, node.right] = [node.right, node.left];
         if (node.right) {
            stack.push(node.right);
         }
         if (node.left) {
            stack.push(node.left);
         }
      }
      return root
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, deque, iteration
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      if (!root) {
         return null
      }

      const queue = new Queue([root]);
      while (!queue.isEmpty()) {
         const node = queue.pop();
         [node.left, node.right] = [node.right, node.left];
         if (node.right) {
            queue.push(node.right);
         }
         if (node.left) {
            queue.push(node.left);
         }
      }
      return root
   };
}


console.log(getTreeValues(new Solution().invertTree(buildTree([2, 1, 3]))), [2, 3, 1])
console.log(getTreeValues(new Solution().invertTree(buildTree([4, 2, 7, 1, 3, 6, 9]))), [4, 7, 2, 9, 6, 3, 1])
console.log(getTreeValues(new Solution().invertTree(buildTree([7, 3, 15, null, null, 9, 20]))), [7, 15, 3, 20, 9])
console.log(getTreeValues(new Solution().invertTree(buildTree([]))), [])