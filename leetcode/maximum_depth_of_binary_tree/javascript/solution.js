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
    *     A: dfs, recursion, post-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      const dfs = (node) => {
         if (node === null) {
            return 0
         }
         const left = dfs(node.left);
         const right = dfs(node.right);
         return 1 + Math.max(left, right)
      }
      return dfs(root)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      if (root === null) {
         return 0
      }
      let mDepth = 1;
      const stack = [[mDepth, root]];

      while (stack.length) {
         const [depth, node] = stack.pop();
         mDepth = Math.max(mDepth, depth);

         if (node.right) {
            stack.push([depth + 1, node.right])
         }
         if (node.left) {
            stack.push([depth + 1, node.left])
         }
      }
      return mDepth
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   maxDepth(root) {
      if (root === null) {
         return 0
      }
      let depth = 0;
      const queue = new Queue([root]);

      while (queue.size()) {
         depth++;
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
      return depth
   };
}


const maxDepth = new Solution().maxDepth;
console.log(new Solution().maxDepth(buildTree([])) === 0)
console.log(new Solution().maxDepth(buildTree([5])) === 1)
console.log(new Solution().maxDepth(buildTree([1, null, 2])) === 2)
console.log(new Solution().maxDepth(buildTree([3, 9, 20, null, null, 15, 7])) === 3)
console.log(new Solution().maxDepth(buildTree([4, 2, 7, 1, 3, 6, 9])) === 3)
