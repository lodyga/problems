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
    * Tags:
    *     DS: binary tree
    *     A: DFS with backtracking, post-order traversal
    * @param {TreeNode} root
    * @param {number} startVal
    * @param {number} destVal
    * @return {string}
    */
   getDirections(root, startVal, destVal) {
      const getLca = (node) => {
         if (node === null) {
            return null
         } else if (
            node.val === startVal ||
            node.val === destVal
         ) {
            return node
         }

         const left = getLca(node.left);
         const right = getLca(node.right);

         if (left && right) {
            return node
         } else {
            return left || right
         }
      };

      const getPath = (node, target) => {

         const backtrack = (node, path) => {
            if (node === null) {
               return ''
            } else if (node.val === target) {
               return path.join('');
            }

            path.push('L');
            const left = backtrack(node.left, path);
            if (left) {
               return left
            }

            path.pop();
            path.push('R');
            const right = backtrack(node.right, path);
            if (right) {
               return right
            }

            path.pop();
         };

         return backtrack(node, [])
      };

      const lca = getLca(root);
      const startPath = getPath(lca, startVal);
      const destPath = getPath(lca, destVal);
      return 'U'.repeat(startPath.length) + destPath
   };
}


const getDirections = new Solution().getDirections;
console.log(new Solution().getDirections(buildTree([2, 1, 3]), 1, 3) === 'UR')
console.log(new Solution().getDirections(buildTree([2, 1]), 2, 1) === 'L')
console.log(new Solution().getDirections(buildTree([5, 1, 2, 3, null, 6, 4]), 3, 6) === 'UURL')
