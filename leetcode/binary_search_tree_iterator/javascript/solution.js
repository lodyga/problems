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


/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, iteration, stack
 * @param {TreeNode} root
 */
class BSTIterator {
   constructor(root) {
      this.node = root;
      this.stack = [];
   };

   /**
   * @return {boolean}
   */
   next() {
      let node = this.node;
      let stack = this.stack;

      while (node) {
         stack.push(node);
         node = node.left;
      }
      node = stack.pop();
      this.node = node.right;1
      return node.val
   };

   /**
    * @return {boolean}
   */
   hasNext() {
      return Boolean(this.node || this.stack.length)
   };
}


/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, iteration, stack
 * @param {TreeNode} root
 */
class BSTIterator {
   constructor(root) {
      this.stack = [];
      let node = root;

      while (node) {
         this.stack.push(node);
         node = node.left;
      }
   };

   /**
   * @return {boolean}
   */
   next() {
      let node = this.stack.pop();
      const val = node.val
      node = node.right;
      
      while (node) {
         this.stack.push(node);
         node = node.left;
      }

      return val
   };

   /**
    * @return {boolean}
   */
   hasNext() {
      return Boolean(this.stack.length)
   };
}


const bstIterator = new BSTIterator(buildTree([5, 6, 7]))
console.log(bstIterator.hasNext())  // return true
console.log(bstIterator.next())  // return 5
console.log(bstIterator.hasNext())  // return true
console.log(bstIterator.next())  // return 6
console.log(bstIterator.hasNext())  // return true
console.log(bstIterator.next())  // return 7
console.log(bstIterator.hasNext())  // return false


const bstIterator2 = new BSTIterator(buildTree([7, 3, 15, null, null, 9, 20]))
console.log(bstIterator2.next())  // return 3
console.log(bstIterator2.next())  // return 7
console.log(bstIterator2.hasNext())  // return true
console.log(bstIterator2.next())  // return 9
console.log(bstIterator2.hasNext())  // return true
console.log(bstIterator2.next())  // return 15
console.log(bstIterator2.hasNext())  // return true
console.log(bstIterator2.next())  // return 20
console.log(bstIterator2.hasNext())  // return false