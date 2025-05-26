class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack, in-order traversal
    * @param {number[]} preorder
    * @param {number[]} inorder
    * @return {TreeNode}
    */
   buildTreeFromPreorderAndInorder(preorder, inorder) {
      if (preorder.length === 0 || inorder.length === 0)
         return

      const node = new TreeNode(preorder[0]);
      const pivot = inorder.indexOf(preorder[0]);
      node.left = buildTreeFromPreorderAndInorder(preorder.slice(1, pivot + 1), inorder.slice(0, pivot));
      node.right = buildTreeFromPreorderAndInorder(preorder.slice(pivot + 1,), inorder.slice(pivot + 1,));
      return node
   };
}
const buildTreeFromPreorderAndInorder = new Solution().buildTreeFromPreorderAndInorder;


console.log(getTreeValues(new Solution().buildTreeFromPreorderAndInorder([1, null, 3], [null, 1, 3])), [1, null, 3])
console.log(getTreeValues(new Solution().buildTreeFromPreorderAndInorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])), [3, 9, 20, null, null, 15, 7])
console.log(getTreeValues(new Solution().buildTreeFromPreorderAndInorder([-1], [-1])), [-1])