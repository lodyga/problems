import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';


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
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      if (!root) {
         return 0
      }
      return (
         1 + Math.max(
            this.maxDepth(root.left),
            this.maxDepth(root.right)
         )
      )
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, stack, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      if (!root) {
         return 0
      }
      let maxTreeDepth = 1;
      const stack = [[root, maxTreeDepth]];

      while (stack.length) {
         let [node, depth] = stack.pop();
         maxTreeDepth = Math.max(maxTreeDepth, depth);

         if (node.right) {
            stack.push([node.right, depth + 1])
         }
         if (node.left) {
            stack.push([node.left, depth + 1])
         }
      }
      return maxTreeDepth
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, deque, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      if (!root) {
         return 0
      }
      let maxTreeDepth = 0;
      const queue = new Queue([root]);

      while (!queue.isEmpty()) {
         maxTreeDepth++;
         const queueSize = queue.size();

         for (let index = 0; index < queueSize; index++) {
            const node = queue.pop();
            if (node.left) {
               queue.push(node.left);
            }
            if (node.right) {
               queue.push(node.right);
            }
         }
      }
      return maxTreeDepth
   };
}


console.log(new Solution().maxDepth(buildTree([])), 0)
console.log(new Solution().maxDepth(buildTree([5])), 1)
console.log(new Solution().maxDepth(buildTree([1, null, 2])), 2)
console.log(new Solution().maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3)