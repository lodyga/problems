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
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      const dfs = (node1, node2) => {
         if (node1 === null && node2 === null) {
            return true
         } else if (node1 === null || node2 === null) {
            return false
         } else if (node1.val !== node2.val) {
            return false
         }

         const left = dfs(node1.left, node2.left);
         const right = dfs(node1.right, node2.right);
         
         return left && right
      }
      return dfs(root1, root2)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, stack
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      const stack = [[root1, root2]];

      while (stack.length) {
         const [node1, node2] = stack.pop();

         if (node1 === null && node2 === null) {
            continue
         } else if (node1 === null || node2 === null) {
            return false
         } else if (node1.val !== node2.val) {
            return false
         }

         stack.push([node1.right, node2.right]);
         stack.push([node1.left, node2.left]);
      }
      return true
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      const queue = new Queue([[root1, root2]]);

      while (queue.size()) {
         const [node1, node2] = queue.pop();

         if (node1 === null && node2 === null) {
            continue
         } else if (node1 === null || node2 === null) {
            return false
         } else if (node1.val !== node2.val) {
            return false
         }

         queue.push([node1.right, node2.right]);
         queue.push([node1.left, node2.left]);
      }
      return true
   };
}


const isSameTree = new Solution().isSameTree;
console.log(new Solution().isSameTree(buildTree([]), buildTree([5])) === false)
console.log(new Solution().isSameTree(buildTree([1, 2, 3]), buildTree([1, 2, 3])) === true)
console.log(new Solution().isSameTree(buildTree([1, 2]), buildTree([1, null, 2])) === false)
console.log(new Solution().isSameTree(buildTree([1, 2, 1]), buildTree([1, 1, 2])) === false)
console.log(new Solution().isSameTree(buildTree([10, 5, 15]), buildTree([10, 5, null, null, 15])) === false)
console.log(new Solution().isSameTree(buildTree([1, null, 2, 3]), buildTree([1, null, 2, null, 3])) === false)
console.log(new Solution().isSameTree(buildTree([4, 2, 7, 1, 3, 6, 9]), buildTree([4, 2, 7, 1, 3, 6, 9])) == true)
