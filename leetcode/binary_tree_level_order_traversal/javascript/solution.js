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
    * Tags: binary tree, bfs, iteration, level order traversal
    * @param {TreeNode} root
    * @return {number[][]}
    */
   levelOrder(root) {
      const queue = new Queue([root]);
      const nodes = [];
      
      while (queue.size()) {
         const queueLength = queue.size();
         const nodeLevel = [];
         
         for (let index = 0; index < queueLength; index++) {
            const node = queue.pop();

            if (node) {
               nodeLevel.push(node.val);
               queue.push(node.left);
               queue.push(node.right);
            }
         }
         if (nodeLevel.length) {
            nodes.push(nodeLevel);
         }
      }
      return nodes
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion, level order traversal
    * @param {TreeNode} root
    * @return {number[][]}
    */
   levelOrder(root) {
      const nodes = [];
      dfs(0, root);
      return nodes

      function dfs(index, node) {
         if (!node) {
            return
         } else if (index === nodes.length) {
            nodes.push([]);
         }

         nodes[index].push(node.val);
         dfs(index + 1, node.left);
         dfs(index + 1, node.right);
      }
   };
}
const levelOrder = new Solution().levelOrder;


console.log(new Solution().levelOrder(buildTree([1, 2, 3])), [[1], [2, 3]])
console.log(new Solution().levelOrder(buildTree([3, 9, 20, null, null, 15, 7])), [[3], [9, 20], [15, 7]])
console.log(new Solution().levelOrder(buildTree([1])), [[1]])
console.log(new Solution().levelOrder(buildTree([])), [])