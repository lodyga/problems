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
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[][]}
    */
   levelOrder(root) {
      if (root === null) {
         return []
      }
      const queue = new Queue([root]);
      const nodes = [];

      while (queue.size()) {
         const queueLength = queue.size();
         const level = [];

         for (let index = 0; index < queueLength; index++) {
            const node = queue.pop();
            level.push(node.val);

            if (node.left)
               queue.push(node.left);
            if (node.right)
               queue.push(node.right);
         }
         nodes.push(level);
      }
      return nodes
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, list
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {number[][]}
    */
   levelOrder(root) {
      const nodes = [];

      const dfs = (index, node) => {
         if (node === null) {
            return
         } else if (index === nodes.length) {
            nodes.push([]);
         }

         nodes[index].push(node.val);
         dfs(index + 1, node.left);
         dfs(index + 1, node.right);
      }
      dfs(0, root);
      return nodes
   };
}


const levelOrder = new Solution().levelOrder;
console.log(JSON.stringify(new Solution().levelOrder(buildTree([1, 2, 3]))) === JSON.stringify([[1], [2, 3]]))
console.log(JSON.stringify(new Solution().levelOrder(buildTree([3, 9, 20, null, null, 15, 7]))) === JSON.stringify([[3], [9, 20], [15, 7]]))
console.log(JSON.stringify(new Solution().levelOrder(buildTree([1]))) === JSON.stringify([[1]]))
console.log(JSON.stringify(new Solution().levelOrder(buildTree([]))) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().levelOrder(buildTree([4, 2, 7, 1, 3, 6, 9]))) == JSON.stringify([[4], [2, 7], [1, 3, 6, 9]]))
