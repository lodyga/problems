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
    * Tags: binary tree, dfs, recursion, post-order traversal
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} q
    * @return {number}
    */
   lowestCommonAncestor(root, p, q) {
      const dfs = (node) => {
         if (node === null)
            return
         else if (
            node === p ||
            node === q
         )
            return node

         const left = dfs(node.left);
         const right = dfs(node.right);

         if (left && right)
            return node
         return left || right
      }
      return dfs(root)
   };
}


class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion, post-order traversal
    * Compare node values, not nodes themselves.
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} q
    * @return {number}
    */
   lowestCommonAncestor(root, p, q) {
      const dfs = (node) => {
         if (node === null)
            return
         else if (
            node.val === p.val ||
            node.val === q.val
         )
            return node.val

         const left = dfs(node.left);
         const right = dfs(node.right);

         if (left && right)
            return node.val
         return left || right
      }
      return dfs(root)
   };
}


const lowestCommonAncestor = new Solution().lowestCommonAncestor;
let [root, lookup] = buildTree([2, 1], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(1), lookup.get(2)).val === 2);

[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(5), lookup.get(1)).val === 3);

[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(6), lookup.get(2)).val === 5);

[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(5), lookup.get(4)).val === 5);

// console.log(new Solution().lowestCommonAncestor(buildTree([2, 1]), buildTree([2]), buildTree([1])) === 2)
// console.log(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([5]), buildTree([1])) === 3)
// console.log(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([6]), buildTree([2])) === 5)
// console.log(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([5]), buildTree([4])) === 5)
