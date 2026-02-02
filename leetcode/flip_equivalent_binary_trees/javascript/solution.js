import { TreeNode, buildTree } from '../../../../JS/binary-tree.js';


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
   static flipEquiv(root1, root2) {
      if (root1 === root2) {
         return true
      } else if (root1 === null || root2 === null) {
         return (root1 === null && root2 === null)
      } else if (root1.val !== root2.val) {
         return false
      } else if (  // not flipped
         flipEquiv(root1.left, root2.left) &&
         flipEquiv(root1.right, root2.right)
      ) {
         return true
      } else if (  // flipped
         flipEquiv(root1.left, root2.right) &&
         flipEquiv(root1.right, root2.left)
      ) {
         return true
      } else {
         return false
      }
   };
}


const flipEquiv = Solution.flipEquiv;
console.log(Solution.flipEquiv(buildTree([1]), buildTree([1])) === true)
console.log(Solution.flipEquiv(buildTree([1, 2, 3, 4, 5, 6, null, null, null, 7, 8]), buildTree([1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7])) === true)
console.log(Solution.flipEquiv(buildTree([]), buildTree([])) === true)
console.log(Solution.flipEquiv(buildTree([]), buildTree([1])) === false)
