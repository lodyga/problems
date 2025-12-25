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
 * Time complexity:
 *     next: Amortized O(1)
 *     hasNext: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, iteration, stack
 * @param {TreeNode} root
 * @returns {BSTIterator}
 */
class BSTIterator {
   /**
    * @constructor
    * @param {TreeNode} root 
    */
   constructor(root) {
      this.root = root;
      this.iterator = this._generateNextNodes();
      const first = this.iterator.next();
      this.nextNode = first.done ? null : first.value;
   }

   /**
    * @returns {IterableIterator<TreeNode>}
    */
   *_generateNextNodes() {
      function* dfs(node) {
         if (node === null) return;

         yield* dfs(node.left);
         yield node;
         yield* dfs(node.right);
      }

      yield* dfs(this.root);
   }

   /**
    * @returns {number}
    */
   next() {
      const value = this.nextNode.val;
      const next = this.iterator.next();
      this.nextNode = next.done ? null : next.value;
      return value;
   }

   /**
    * @returns {boolean}
    */
   hasNext() {
      return this.nextNode !== null;
   }
}


/**
 * Time complexity:
 *     next: Amortized O(1)
 *     hasNext: O(1)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: binary tree
 *     A: dfs, iteration, pre-order traversal, in-order traversal
 * @param {TreeNode} root
 */
class BSTIterator {
   constructor(root) {
      this.stack = [];
      this._pushLeft(root);
   };

   /**
   * @param {TreeNode}
   */
   _pushLeft(node) {
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
      const val = node.val;
      node = node.right;
      this._pushLeft(node);
      return val
   };

   /**
    * @return {boolean}
   */
   hasNext() {
      return this.stack.length > 0
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
      this.node = root;
      this.stack = [];
   };

   /**
    * @return {number}
    */
   next() {
      if (!this.hasNext())
         return null
      return this._getNext()
   };

   /**
    * @return {boolean}
    */
   hasNext() {
      return Boolean(this.node || this.stack.length)
   };

   /**
    * @return {number}
    */
   _getNext() {
      let node = this.node;
      const stack = this.stack;

      while (node) {
         stack.push(node);
         node = node.left;
      }
      node = stack.pop();
      this.node = node.right;
      return node.val
   };
}


const bstIterator = new BSTIterator(buildTree([6, 5, 7]))
console.log(bstIterator.hasNext() === true)
console.log(bstIterator.next() === 5)
console.log(bstIterator.hasNext() === true)
console.log(bstIterator.next() === 6)
console.log(bstIterator.hasNext() === true)
console.log(bstIterator.next() === 7)
console.log(bstIterator.hasNext() === false)


const bstIterator2 = new BSTIterator(buildTree([7, 3, 15, null, null, 9, 20]))
console.log(bstIterator2.next() === 3)
console.log(bstIterator2.next() === 7)
console.log(bstIterator2.hasNext() === true)
console.log(bstIterator2.next() === 9)
console.log(bstIterator2.hasNext() === true)
console.log(bstIterator2.next() === 15)
console.log(bstIterator2.hasNext() === true)
console.log(bstIterator2.next() === 20)
console.log(bstIterator2.hasNext() === false)
