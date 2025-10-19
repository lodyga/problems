class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {}
    * @return {}
    */
   () {

   };
}


print(Solution().nextPermutation([1, 2, 3, 6, 5, 4]) == [1, 2, 4, 3, 5, 6])
print(Solution().nextPermutation([1, 2, 3]) == [1, 3, 2])
print(Solution().nextPermutation([3, 2, 1]) == [1, 2, 3])
print(Solution().nextPermutation([1, 1, 5]) == [1, 5, 1])
print(Solution().nextPermutation([1, 2, 3, 4]) == [1, 2, 4, 3])
print(Solution().nextPermutation([1, 3, 2, 4]) == [1, 3, 4, 2])
print(Solution().nextPermutation([1, 2, 4, 3]) == [1, 3, 2, 4])
print(Solution().nextPermutation([4, 3, 2, 1]) == [1, 2, 3, 4])
print(Solution().nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4])
print(Solution().nextPermutation([1, 3, 4, 2]) == [1, 4, 2, 3])