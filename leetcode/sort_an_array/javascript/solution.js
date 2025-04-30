import { MinPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags: heap, sorting
   * @param {number[]} numbers
   * @return {number[]}
   */
  sortArray(numbers) {
    const numberHeap = new MinPriorityQueue();
    numbers.forEach(number => numberHeap.enqueue(number));
    const sortedNumbers = [];
    while (numberHeap.size()) {
      sortedNumbers.push(numberHeap.dequeue());
    }
    return sortedNumbers
  };
}
const sortArray = new Solution().sortArray;


class Solution {
  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags: merge sort, sorting
   * @param {number[]} numbers
   * @return {number[]}
   */
  sortArray(numbers) {
    function mergeSort(left, right) {
      if (left === right) {
        return
      }
      divide(left, right);
      merge(left, right);
    }

    function divide(left, right) {
      const middle = (left + right) / 2 | 0;
      mergeSort(left, middle);
      mergeSort(middle + 1, right);
    }

    function merge(left, right) {
      const middle = (left + right) / 2 | 0;
      const leftChunk = numbers.slice(left, middle + 1);
      const rightChunk = numbers.slice(middle + 1, right + 1);
      let index = left;
      left = 0;
      right = 0;

      while (
        left < leftChunk.length &&
        right < rightChunk.length
      ) {
        if (leftChunk[left] <= rightChunk[right]) {
          numbers[index] = leftChunk[left];
          left++;
        } else {
          numbers[index] = rightChunk[right];
          right++;
        }
        index++;
      }
      while (left < leftChunk.length) {
        numbers[index] = leftChunk[left];
        left++;
        index++;
      }
      while (right < rightChunk.length) {
        numbers[index] == rightChunk[right];
        right++;
        index++;
      }
    }

    mergeSort(0, numbers.length - 1);
    return numbers
  }
}


class Solution {
  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags: quick sort, sorting, tle
   * @param {number[]} numbers
   * @return {number[]}
   */
  sortArray(numbers) {
    function quickSort(left, right) {
      if (left >= right) {
        return
      }

      const pivot = partition(left, right)
      quickSort(left, pivot - 1);
      quickSort(pivot + 1, right);
    };

    function partition(left, end) {
      const pivot = numbers[end];
      left--;

      for (let right = left + 1; right < end; right++) {
        if (numbers[right] < pivot) {
          left++;
          swapNumbers(left, right);
        }
      }
      swapNumbers(left + 1, end);
      return left + 1
    }

    function swapNumbers(left, right) {
      [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
    }

    quickSort(0, numbers.length - 1);
    return numbers
  }
}

class Solution {
  /**
   * Time complexity: O(n2)
   * Auxiliary space complexity: O(1)
   * Tags: insertion sort, sorting, tle
   * @param {number[]} numbers
   * @return {number[]}
   */
  sortArray(numbers) {
    function insertionSort() {
      for (let right = 1; right < numbers.length; right++) {
        const key = numbers[right];
        let left = right - 1;

        while (
          left >= 0 &&
          numbers[left] > key
        ) {
          numbers[left + 1] = numbers[left];
          left--;
        }
        numbers[left + 1] = key;
      }
    }
    insertionSort();
    return numbers
  }
}


class Solution {
  /**
   * Time complexity: O(n2)
   * Auxiliary space complexity: O(1)
   * Tags: bubble sort, sorting, tle
   * @param {number[]} numbers
   * @return {number[]}
   */
  sortArray(numbers) {
     function bubbleSort() {
        for (let i = 0; i < numbers.length - 1; i++) {
           for (let j = 0; j < numbers.length - 1 - i; j++) {
              if (numbers[j] > numbers[j + 1]) {
                 [numbers[j], numbers[j + 1]] = [numbers[j + 1], numbers[j]];
              }
           }
        }
     }
     bubbleSort();
     return numbers
  };
}


console.log(new Solution().sortArray([4]), [4])
console.log(new Solution().sortArray([5, 4]), [4, 5])
console.log(new Solution().sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
console.log(new Solution().sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])
console.log(new Solution().sortArray([-2, 3, -5]), [-5, -2, 3])