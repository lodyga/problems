import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { ListNode, areLinkedListsEqueal, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'


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
 * Represents a node in a singly-linked list.
 * class ListNode {
 *    constructor(val = null, next = null) {
 *       this.val = val;
 *       this.next = next;
 *    }
 * }
 */


class Solution {
   /**
    * Time complexity: O(n * m)
    *     n: list size
    *     m: tree size
    * Auxiliary space complexity: O(m)
    * Tags:
    *     DS: linked list, binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {ListNode  } head
    * @param {TreeNode} root
    * @return {boolean} 
    */
   static isSubPath(head, root) {
      const dfs = (head, root) => {
         if (head === null) {
            return true
         } else if (root === null) {
            return false
         } else if (head.val === root.val) {
            return (
               dfs(head.next, root.left) ||
               dfs(head.next, root.right)
            )
         }

         return false
      };

      if (head === null) {
         return true
      } else if (root === null) {
         return false
      } else if (dfs(head, root)) {
         return true
      }

      return (
         isSubPath(head, root.left) ||
         isSubPath(head, root.right)
      )
   };
}


const isSubPath = Solution.isSubPath;
console.log(Solution.isSubPath(buildLinkedList([1, 2]), buildTree([1, 2, 3])) == true)
console.log(Solution.isSubPath(buildLinkedList([2, 3]), buildTree([1, 2, 4, 3])) == true)
console.log(Solution.isSubPath(buildLinkedList([4, 2, 8]), buildTree([1, 4, 4, null, 2, 2, null, 1, null, 6, 8, null, null, null, null, 1, 3])) == true)
console.log(Solution.isSubPath(buildLinkedList([1, 4, 2, 6]), buildTree([1, 4, 4, null, 2, 2, null, 1, null, 6, 8, null, null, null, null, 1, 3])) == true)
console.log(Solution.isSubPath(buildLinkedList([1, 4, 2, 6, 8]), buildTree([1, 4, 4, null, 2, 2, null, 1, null, 6, 8, null, null, null, null, 1, 3])) == false)
console.log(Solution.isSubPath(buildLinkedList([4, 2]), buildTree([4, 4, 4, 1, null, null, null, 2])) == false)
