# Design Compressed String Iterator
https://neetcode.io/solutions/design-compressed-string-iterator
https://leetcode.com/problems/design-compressed-string-iterator

<p>
Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:
- next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
- hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
</p>

<pre>
<b>Example 1:</b>
Input
["StringIterator","next","next","next","next","next","next","next", "hasNext", "next", "hasNext", "next"]
[["L1e2t1C1o1d1e1"],[],[],[],[],[],[],[],[],[],[],[]]
Output
[null,"L","e","e","t","C","o","d",true,"e",false," "]

Explanation
StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
</pre>
