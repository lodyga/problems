/**
 * Time complexity: 
 *    set(): O(1)
 *    get(): O(logn)
 *    n: max `values assigned to a key` count
 * Auxiliary space complexity: O(n*m)
 *     m: key count
 * Tags: binary search
 * @param {}
 * @return {}
 */
class TimeMap {
   constructor() {
      this.store = new Map();
   };

   /** 
    * @param {string} key 
    * @param {string} value 
    * @param {number} timestamp
    * @return {void}
    */
   set(key, value, timestamp) {
      if (!this.store.has(key)) {
         this.store.set(key, [])
      }
      this.store.get(key).push([timestamp, value]);  // [timestamp, value]
   };

   /** 
    * @param {string} key 
    * @param {number} timestamp
    * @return {string}
    */
   get(key, timestamp) {
      if (
         !this.store.get(key) ||
         timestamp < this.store.get(key)[0][0]
      ) {
         return ''
      }
      const list_values = this.store.get(key);
      
      if (timestamp >= list_values[list_values.length - 1][0]) {
         return list_values[list_values.length - 1][1]
      }
      let left = 0;
      let right = list_values.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleTimeStamp = list_values[middle][0];

         if (timestamp === middleTimeStamp) {
            return list_values[middle][1]
         } else if (timestamp < middleTimeStamp) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return list_values[right][1]
   }
}


class ListNode {
   constructor(val = [null, null], next = null) {
      this.val = val;  // [timestamp, value]
      this.next = next;
   }
}

/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 *     n: max `values assigned to a key` count
 * Auxiliary space complexity: O(n*m)
 *     m: key count
 * Tags: linked list
 * @param {}
 * @return {}
 */
class TimeMap {
   constructor() {
      this.store = new Map();
   };

   /** 
    * @param {string} key 
    * @param {string} value 
    * @param {number} timestamp
    * @return {void}
    */
   set(key, value, timestamp) {
      if (!this.store.has(key)) {
         this.store.set(key, new ListNode([timestamp, value], null));
         return
      }
      let node = this.store.get(key);
      while (node.next) {
         node = node.next;
      }
      node.next = new ListNode([timestamp, value], null);
   };

   /** 
    * @param {string} key 
    * @param {number} timestamp
    * @return {string}
    */
   get(key, timestamp) {
      if (!this.store.get(key))
         return ''
      let node = this.store.get(key);

      while (node.next && timestamp >= node.next.val[0]) {
         node = node.next;
      }

      return timestamp >= node.val[0] ? node.val[1] : ''
   }
}


// Example 1
const timeMap = new TimeMap();
timeMap.set('foo', 'bar', 1);  // store the key 'foo' and value 'bar' along with timestamp = 1.
console.log(timeMap.get('foo', 1));  // return 'bar'
console.log(timeMap.get('foo', 3));  // return 'bar', since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is 'bar'.
timeMap.set('foo', 'bar2', 4);  // store the key 'foo' and value 'bar2' along with timestamp = 4.
console.log(timeMap.get('foo', 4));  // return 'bar2'
console.log(timeMap.get('foo', 5));  // return 'bar2'

// Example 2
const timeMap2 = new TimeMap();
timeMap2.set('love', 'high', 10);
timeMap2.set('love', 'low', 20);
console.log(timeMap2.get('love', 5));  // return ''
console.log(timeMap2.get('love', 10));  // return high
console.log(timeMap2.get('love', 15));  // return high
console.log(timeMap2.get('love', 20));  // return low
console.log(timeMap2.get('love', 25));  // return low

// Example 3
const timeMap3 = new TimeMap();
timeMap3.set('a', 'bar', 1);
timeMap3.set('x', 'b', 3);
console.log(timeMap3.get('b', 3));  // return ''
timeMap3.set('foo', 'bar2', 4);
console.log(timeMap3.get('foo', 4));  // return 'bar2'
console.log(timeMap3.get('foo', 5));  // return 'bar2'