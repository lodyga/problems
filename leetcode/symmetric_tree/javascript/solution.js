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
   isSymmetric(root) {
      const dfs = (node1, node2) => {
         if (node1 === null || node2 === null) {
            return node1 === null && node2 === null
         }

         return (
            node1.val === node2.val &&
            dfs(node1.left, node2.right) &&
            dfs(node1.right, node2.left)
         )
      }

      return dfs(root.left, root.right)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {boolean}
    */
   isSymmetric(root) {
      const stack = [];
      stack.push([root.left, root.right]);

      while (stack.length) {
         const [left, right] = stack.pop();

         if (left === null && right === null) {
            continue
         } else if (
            left === null || right === null ||
            left.val !== right.val
         ) {
            return false
         }

         stack.push([left.left, right.right]);
         stack.push([left.right, right.left]);
      }

      return true
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: bfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {boolean}
    */
   isSymmetric(root) {
      const queue = new Queue();
      queue.enqueue([root.left, root.right]);

      while (queue.size()) {
         const [left, right] = queue.dequeue();

         if (left === null && right === null) {
            continue
         } else if (
            left === null || right === null ||
            left.val !== right.val
         ) {
            return false
         }

         queue.enqueue([left.left, right.right]);
         queue.enqueue([left.right, right.left]);
      }

      return true
   };
}



const isSymmetric = new Solution().isSymmetric;
console.log(new Solution().isSymmetric(buildTree([1, 2, 2, 3, 4, 4, 3])) == true)
console.log(new Solution().isSymmetric(buildTree([1, 2, 2, null, 3, null, 3])) == false)
