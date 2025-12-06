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
    *     side effect
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      let counter = 0;

      const dfs = (node, prevMax) => {
         if (node === null)
            return

         prevMax = Math.max(prevMax, node.val);
         counter += node.val >= prevMax ? 1 : 0;
         dfs(node.left, prevMax);
         dfs(node.right, prevMax);
      }
      dfs(root, root.val)
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    *     pure function
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      const dfs = (node, prevMax) => {
         if (node === null) {
            return 0
         }
         prevMax = Math.max(prevMax, node.val);
         const isGood = node.val >= prevMax ? true : false;
         const left = dfs(node.left, prevMax);
         const right = dfs(node.right, prevMax);
         return isGood + left + right
      }
      return dfs(root, root.val)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      const stack = [[root, root.val]];
      let counter = 0;

      while (stack.length) {
         let [node, prevMax] = stack.pop();
         prevMax = Math.max(prevMax, node.val);
         counter += node.val >= prevMax ? 1 : 0;

         if (node.left)
            stack.push([node.left, prevMax]);
         if (node.right)
            stack.push([node.right, prevMax]);
      }
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      const queue = new Queue([[root, root.val]]);
      let counter = 0;

      while (queue.size()) {
         let [node, prevMax] = queue.pop();
         prevMax = Math.max(prevMax, node.val);
         counter += node.val >= prevMax ? 1 : 0;

         if (node.left)
            queue.push([node.left, prevMax]);
         if (node.right)
            queue.push([node.right, prevMax]);
      }
      return counter
   };
}


const goodNodes = new Solution().goodNodes;
console.log(new Solution().goodNodes(buildTree([1])) === 1)
console.log(new Solution().goodNodes(buildTree([1, 2, 3])) === 3)
console.log(new Solution().goodNodes(buildTree([3, 1, 4, 3, null, 1, 5])) === 4)
console.log(new Solution().goodNodes(buildTree([3, 3, null, 4, 2])) === 3)
