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
    * @return {boolean}
    */
   isCompleteTree(root) {
      const queue = new Queue([root]);
      let wasNull = false;

      while (queue.size()) {
         const node = queue.dequeue();

         if (wasNull && node !== null) {
            return false
         } else if (node === null) {
            wasNull = true;
            continue
         }

         queue.enqueue(node.left);
         queue.enqueue(node.right);
      }

      return true
   };
}


const isCompleteTree = new Solution().isCompleteTree;
console.log(new Solution().isCompleteTree(buildTree([1, 2, 3, 4, 5, 6])) === true)
console.log(new Solution().isCompleteTree(buildTree([1, 2, 3, 4, 5, null, 7])) === false)
console.log(new Solution().isCompleteTree(buildTree([1])) === true)
console.log(new Solution().isCompleteTree(buildTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, null, null, 15])) === false)
