import { Queue } from '@datastructures-js/queue';


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      function dfs(node1, node2) {
         if (!node1 && !node2) {
            return true
         } else if (
            !node1 ||
            !node2 ||
            node1.val != node2.val
         ) {
            return false
         }
         return (
            dfs(node1.left, node2.left) &&
            dfs(node1.right, node2.right)
         )
      }
      return dfs(root1, root2)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      const stack1 = [root1];
      const stack2 = [root2];

      while (stack1.length || stack2.length) {
         const node1 = stack1.pop();
         const node2 = stack2.pop();

         if (!node1 && !node2) {
            continue
         } else if (
            !node1 ||
            !node2 ||
            node1.val != node2.val
         ) {
            return false
         }
         stack1.push(node1.right);
         stack2.push(node2.right);
         stack1.push(node1.left);
         stack2.push(node2.left);
      }
      return true
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSameTree(root1, root2) {
      const stack1 = new Queue([root1]);
      const stack2 = new Queue([root2]);

      while (!stack1.isEmpty() || !stack2.isEmpty()) {
         const node1 = stack1.pop();
         const node2 = stack2.pop();

         if (!node1 && !node2) {
            continue
         } else if (
            !node1 ||
            !node2 ||
            node1.val != node2.val
         ) {
            return false
         }
         stack1.push(node1.right);
         stack2.push(node2.right);
         stack1.push(node1.left);
         stack2.push(node2.left);
      }
      return true
   };
}


console.log(new Solution().isSameTree(buildTree([]), buildTree([5])), false)
console.log(new Solution().isSameTree(buildTree([1, 2, 3]), buildTree([1, 2, 3])), true)
console.log(new Solution().isSameTree(buildTree([1, 2]), buildTree([1, null, 2])), false)
console.log(new Solution().isSameTree(buildTree([1, 2, 1]), buildTree([1, 1, 2])), false)
console.log(new Solution().isSameTree(buildTree([10, 5, 15]), buildTree([10, 5, null, null, 15])), false)
console.log(new Solution().isSameTree(buildTree([1, null, 2, 3]), buildTree([1, null, 2, null, 3])), false)