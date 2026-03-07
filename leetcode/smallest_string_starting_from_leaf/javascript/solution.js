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
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: binary tree, list
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {string}
    */
   smallestFromLeaf(root) {
      const paths = [];

      const dfs = (node, path) => {
         if (node === null) {
            return
         }

         const letter = String.fromCharCode(node.val + 'a'.charCodeAt(0));
         path = letter + path;

         if (node.left === null && node.right === null) {
            paths.push(path);
            return
         }

         dfs(node.left, path);
         dfs(node.right, path);
      }

      dfs(root, '')
      return paths.reduce((prevPath, path) => prevPath < path ? prevPath : path);
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: binary tree, list
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {string}
    */
   smallestFromLeaf(root) {
      const dfs = (node, path) => {
         if (node === null) {
            return
         }

         const letter = String.fromCharCode(node.val + 'a'.charCodeAt(0));
         path = letter + path;

         if (node.left && node.right) {
            return [dfs(node.left, path), dfs(node.right, path)].sort()[0]
         } else if (node.left || node.right) {
            return (
               dfs(node.left, path) ||
               dfs(node.right, path)
            )
         }

         return path
      }

      return dfs(root, '')
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: binary tree, list
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {string}
    */
   smallestFromLeaf(root) {
      const dfs = (node, path) => {
         if (node === null) {
            return
         }

         const letter = String.fromCharCode(node.val + 'a'.charCodeAt(0));
         path = letter + path;

         if (node.left && node.right) {
            return [dfs(node.left, path), dfs(node.right, path)].sort()[0]
         } else if (node.left) {
            return dfs(node.left, path)
         } else if (node.right) {
            return dfs(node.right, path)
         }

         return path
      }

      return dfs(root, '')
   };
}


const smallestFromLeaf = new Solution().smallestFromLeaf;
console.log(new Solution().smallestFromLeaf(buildTree([0, 1, 2, 3, 4, 3, 4])) === 'dba')
console.log(new Solution().smallestFromLeaf(buildTree([25, 1, 3, 1, 3, 0, 2])) === 'adz')
console.log(new Solution().smallestFromLeaf(buildTree([2, 2, 1, null, 1, 0, null, 0])) === 'abc')
console.log(new Solution().smallestFromLeaf(buildTree([0, null, 1])) === 'ba')
