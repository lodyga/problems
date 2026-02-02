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
    *     A: dfs, recursion, post-order traversal
    * Compare node objects, not just nodes values.
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


const lowestCommonAncestor = new Solution().lowestCommonAncestor;
// Compare node objects
let [root, lookup] = buildTree([4, 5, 6], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(5), lookup.get(6)) === lookup.get(4));
[root, lookup] = buildTree([4, 5], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(4), lookup.get(5)) === lookup.get(4));
[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(5), lookup.get(1)) === lookup.get(3));
[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(6), lookup.get(2)) === lookup.get(5));
[root, lookup] = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], { withLookup: true });
console.log(new Solution().lowestCommonAncestor(root, lookup.get(5), lookup.get(4)) === lookup.get(5));


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, post-order traversal
    * Compare node values, not nodes objects.
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
            return node

         const left = dfs(node.left);
         const right = dfs(node.right);

         if (left && right)
            return node
         return left || right
      }
      const res = dfs(root);
      res.left = null;
      res.right = null;
      return res
   };
}


const lowestCommonAncestor = new Solution().lowestCommonAncestor;
// Compare node values
console.log(isSameTree(new Solution().lowestCommonAncestor(buildTree([4, 5, 6]), buildTree([5]), buildTree([6])), buildTree([4])))
console.log(isSameTree(new Solution().lowestCommonAncestor(buildTree([4, 5]), buildTree([4]), buildTree([5])), buildTree([4])))
console.log(isSameTree(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([5]), buildTree([1])), buildTree([3])))
console.log(isSameTree(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([6]), buildTree([2])), buildTree([5])))
console.log(isSameTree(new Solution().lowestCommonAncestor(buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), buildTree([5]), buildTree([4])), buildTree([5])))
