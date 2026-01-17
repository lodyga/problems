import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { Queue } from '@datastructures-js/queue';


/**
 * class TreeNode {
 *    constructor(val = null, left = null, right = null) {
 *       this.val = val
 *       this.left = left
 *       this.right = right
 *    };
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      const dfs = (node) => {
         if (node === null) {
            return
         }
         [node.left, node.right] = [node.right, node.left];
         dfs(node.right);
         dfs(node.left);
      }
      dfs(root)
      return root
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      if (root === null) {
         return null
      }

      const stack = [root];

      while (stack.length) {
         const node = stack.pop();
         [node.left, node.right] = [node.right, node.left];
         if (node.left) {
            stack.push(node.left);
         }
         if (node.right) {
            stack.push(node.right);
         }
      }
      return root
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   invertTree(root) {
      if (root === null) {
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


const invertTree = new Solution().invertTree;
console.log(JSON.stringify(getTreeValues(new Solution().invertTree(buildTree([2, 1, 3])))) === JSON.stringify([2, 3, 1]))
console.log(JSON.stringify(getTreeValues(new Solution().invertTree(buildTree([4, 2, 7, 1, 3, 6, 9])))) === JSON.stringify([4, 7, 2, 9, 6, 3, 1]))
console.log(JSON.stringify(getTreeValues(new Solution().invertTree(buildTree([7, 3, 15, null, null, 9, 20])))) === JSON.stringify([7, 15, 3, 20, 9]))
console.log(JSON.stringify(getTreeValues(new Solution().invertTree(buildTree([])))) === JSON.stringify([]))
