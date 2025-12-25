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
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   leafSimilar(root1, root2) {
      const dfs = (node, leafList) => {
         if (node === null) {
            return
         } else if (
            node.left === null &&
            node.right === null
         ) {
            leafList.push(node.val);
            return
         }
         dfs(node.left, leafList);
         dfs(node.right, leafList);
      }
      const leaves1 = [];
      dfs(root1, leaves1);
      const leaves2 = [];
      dfs(root2, leaves2);
      return leaves1.toString() === leaves2.toString();
   };
}


const leafSimilar = new Solution().leafSimilar;
console.log(new Solution().leafSimilar(buildTree([1, 2]), buildTree([2, 2])) === true)
console.log(new Solution().leafSimilar(buildTree([1, 2, 3]), buildTree([1, 3, 2])) === false)
console.log(new Solution().leafSimilar(buildTree([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), buildTree([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8])) === true)
console.log(new Solution().leafSimilar(buildTree([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 11, null, null, 8, 10]), buildTree([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4])) === false)
console.log(new Solution().leafSimilar(buildTree([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), buildTree([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 11, null, null, 8, 10])) === false)
console.log(new Solution().leafSimilar(buildTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 8, 9]), buildTree([1, 2, 3, 10, 11, 12, 13])) === false)
