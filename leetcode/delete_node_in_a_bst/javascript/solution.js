import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';


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
    * Tags: binary tree
    * @param {TreeNode} root
    * @param {number} key
    * @return {TreeNode}
   */
   static deleteNode(root, key) {
      const dfs = (node) => {
         if (node === null) {
            return node
         }
         else if (key == node.val) {
            if (!node.right) {
               node = node.left;
            } else if (!node.left) {
               node = node.right;
            } else {
               let bottom_node = node.right;
               while (bottom_node.left) {
                  bottom_node = bottom_node.left;
               }
               node.val = bottom_node.val;
               node.right = deleteNode(node.right, node.val)
            }
         }
         else if (key < node.val) {
            node.left = dfs(node.left)
         }
         else {
            node.right = dfs(node.right)
         }
         return node
      }
      
      return dfs(root)
   };
}


// Bind the method to the instance
// const solution = new Solution();
// const deleteNode = solution.deleteNode.bind(solution); // Bind the context

// static method
const deleteNode = Solution.deleteNode;
console.log(isSameTree(Solution.deleteNode(buildTree([5, 3, 6]), 6), buildTree([5, 3])))
console.log(isSameTree(Solution.deleteNode(buildTree([5, 3, 6]), 3), buildTree([5, null, 6])))
console.log(isSameTree(Solution.deleteNode(buildTree([5, 3, 6]), 5), buildTree([6, 3])))
console.log(isSameTree(Solution.deleteNode(buildTree([5, 3, 6, 2, 4, null, 7]), 3), buildTree([5, 4, 6, 2, null, null, 7])))
console.log(isSameTree(Solution.deleteNode(buildTree([5, 3, 6, 2, 4, null, 7]), 0), buildTree([5, 3, 6, 2, 4, null, 7])))
console.log(isSameTree(Solution.deleteNode(buildTree([]), 0), buildTree([])))
console.log(isSameTree(Solution.deleteNode(buildTree([0]), 0), buildTree([])))
